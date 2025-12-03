from fastapi import APIRouter, Depends
from sqlmodel import Field, Session
from typing import Annotated
from src.db.db import get_session
from src.db.models import Book

router=APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]
@router.get("/")
def read_books(id: int, session: Session = Depends(get_session)):
    return session.get(Book, id)

@router.post("/")
def create_books(book: Book, session: Session = Depends(get_session)) -> Book:
    session.add(book)
    session.commit()
    return book