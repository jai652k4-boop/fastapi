from fastapi import APIRouter
from .schema import UserCreateModel

auth_router = APIRouter()

@auth_router.post('/sign-up')
async def create_user_account(user_data: UserCreateModel):
    pass