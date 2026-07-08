from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate


def create_user(
    db: Session,
    user: UserCreate
):

    new_user = User(
        nome=user.nome,
        email=user.email,
        senha=user.senha,
        cargo=user.cargo
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



def get_users(db: Session):

    return db.query(User).all()