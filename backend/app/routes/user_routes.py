from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.connection import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_users,
    update_user,
    delete_user,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
)
def create(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user(db, user)


@router.get(
    "/",
    response_model=list[UserResponse],
)
def list_users(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_users(db)


@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update(
    user_id: int,
    user: UserCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return update_user(
        db=db,
        user_id=user_id,
        user_data=user,
    )


@router.delete(
    "/{user_id}",
)
def delete(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return delete_user(
        db=db,
        user_id=user_id,
    )