from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession

from .schema import userModel, UserCreateModel
from .service import UserService
from db.main import get_session

auth_router = APIRouter()
user_service = UserService()
DBSesssion = Annotated[AsyncSession, Depends(get_session)]


@auth_router.post(
    "/sign-up", response_model=userModel, status_code=status.HTTP_201_CREATED
)
async def create_user_account(user_data: UserCreateModel, session: DBSesssion):
    email = user_data.email

    user_exist = await user_service.user_exist(email, session)

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User is already exist"
        )

    new_user = await user_service.create_user(user_data, session)

    return new_user
