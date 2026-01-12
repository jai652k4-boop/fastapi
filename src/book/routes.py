from fastapi import APIRouter, status, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
import uuid

from db.main import get_session
from .service import BookCreateModel
from book.schema import Book, BookUpdateModel
from book.service import BookService

bookRouter = APIRouter()
book_service = BookService()

@bookRouter.get("/", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


@bookRouter.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session)
) -> dict:

    new_book = await book_service.create_book(book_data, session)

    return new_book


@bookRouter.get("/{book_id}", response_model=Book)
async def get_books_id(
    book_id: uuid.UUID, session: AsyncSession = Depends(get_session)
):
    return await book_service.get_book(book_id, session)


@bookRouter.patch("/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(
    book_id: uuid.UUID,
    update_book_model: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
):

    updated_book = await book_service.update_book(book_id, update_book_model ,session)
    
    if updated_book:
        return updated_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    

@bookRouter.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: uuid.UUID, session: AsyncSession = Depends(get_session)):
    
    book_to_delete = await book_service.delete_book(book_id, session)
    
    if book_to_delete:
        return None
    else:
        raise HTTPException(status_code=404, detail="Book not found")