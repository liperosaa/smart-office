from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.auth.security import hash_password


def create_user(
    db: Session,
    user: UserCreate
):
    # Verifica se já existe usuário com o mesmo e-mail
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="E-mail já cadastrado"
        )

    new_user = User(
        nome=user.nome,
        email=user.email,
        senha_hash=hash_password(user.senha),
        cargo=user.cargo
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(
    db: Session
):
    return db.query(User).all()


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def update_user(
    db: Session,
    user_id: int,
    user_data: UserCreate
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    # Verifica se outro usuário já utiliza esse e-mail
    existing_user = (
        db.query(User)
        .filter(
            User.email == user_data.email,
            User.id != user_id
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="E-mail já cadastrado"
        )

    user.nome = user_data.nome
    user.email = user_data.email
    user.senha_hash = hash_password(user_data.senha)
    user.cargo = user_data.cargo

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "Usuário removido com sucesso"
    }