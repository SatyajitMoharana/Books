from fastapi import APIRouter, Depends
from sqlmodel import Field, Session, select
from typing import Annotated
from src.db.db import get_session
from src.db.models import Book
from src.services import book_service
router=APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

#Read All Books
@router.get("/")
def read_all_books(session: Session = Depends(get_session)) -> list[Book]:
    """Retrieve all books from the database."""
    return  book_service.read_all_books(session)  
    
#Create Dummy Books
@router.post("/add_books")
def create_books_five(session: Session = Depends(get_session)) -> list[Book]:
    """Create five sample books in the database."""
    return book_service.create_books_five(session)

# Create a new book
@router.post("/")
def create_books(book: Book, session: Session = Depends(get_session)) -> Book:
    """Create a new book in the database."""
    return book_service.create_book(book, session)

# Delete a book by ID
@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)) -> str:
    """Delete a book by its ID."""
    return book_service.delete_book(book_id, session)
