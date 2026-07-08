from sqlalchemy.orm import Session
from fastapi import HTTPException

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



def get_users(
    db: Session
):

    return db.query(User).all()



def update_user(
    db: Session,
    user_id: int,
    user_data: UserCreate
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()


    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )


    user.nome = user_data.nome
    user.email = user_data.email
    user.senha = user_data.senha
    user.cargo = user_data.cargo


    db.commit()
    db.refresh(user)

    return user



def delete_user(
    db: Session,
    user_id: int
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()


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

def test_list_users(client):
    response = client.get("/users/")

    assert response.status_code == 200