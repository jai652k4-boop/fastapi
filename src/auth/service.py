from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc

from .models import User
from .schema import UserCreateModel
from .utils import generate_passwd_hash, verify_password

class UserService:
    
    async def get_user_by_email(self,email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)
        
        result = await session.exec(statement)
        
        user = result.first()
        
        return user
    
    async def user_exist(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email, session)
        
        return True if user is not None else False
    
    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        data = user_data.model_dump(exclude={"password"})
        
        raw_password = user_data.password
        data["password_hash"] = generate_passwd_hash(raw_password)
        
        new_user = User(
            **data
        )
                
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        
        return new_user
        