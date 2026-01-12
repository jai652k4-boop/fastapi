from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
import uuid

from .schema import BookCreateModel, BookUpdateModel
from .models import Book
from .exceptions import BookNotFoundException


class BookService:

    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_book(self, id: uuid.UUID, session: AsyncSession):
        statement = select(Book).where(Book.id == id.bytes)
        result = await session.exec(statement)
        book = result.first()

        if not book:
            raise BookNotFoundException()

        return book

    async def create_book(
        self,
        book_data: BookCreateModel,
        session: AsyncSession
    ):
        new_book = Book(**book_data.model_dump())

        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)

        return new_book

    async def update_book(
        self,
        id: uuid.UUID,
        update_book: BookUpdateModel,
        session: AsyncSession
    ):
        book_to_update = await self.get_book(id, session)

        update_data = update_book.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(book_to_update, key, value)

        await session.commit()
        await session.refresh(book_to_update)

        return book_to_update

    async def delete_book(self, id: uuid.UUID, session: AsyncSession):
        book_to_delete = await self.get_book(id, session)

        await session.delete(book_to_delete)
        await session.commit()

        return {"message": "Book deleted successfully"}
