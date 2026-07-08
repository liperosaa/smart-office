from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_database
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_users,
    update_user,
    delete_user
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse
)
def create(
    user: UserCreate,
    db: Session = Depends(get_database)
):

    return create_user(db, user)



@router.get(
    "/",
    response_model=list[UserResponse]
)
def list_users(
    db: Session = Depends(get_database)
):

    return get_users(db)

@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_database)
):

    return update_user(
        db,
        user_id,
        user
    )


@router.delete(
    "/{user_id}"
)
def delete(
    user_id: int,
    db: Session = Depends(get_database)
):

    return delete_user(
        db,
        user_id
    )