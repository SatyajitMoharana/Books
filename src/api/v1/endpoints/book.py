from fastapi import APIRouter, Depends
from sqlmodel import Field, Session, select
from typing import Annotated
from src.db.db import get_session
from src.db.models import Book
from src.services import book_service
router=APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

#Read All Books
@router.get("/",
summary="Read All Books",
description="Read all books from the database.",
response_model=list[Book],
status_code=200
)
def read_all_books(session: Session = Depends(get_session)) -> list[Book]:
    """Retrieve all books from the database."""
    return  book_service.read_all_books(session)  
 
#Read Book by ID
@router.get("/{book_id}",
summary="Read Book by ID",
description="Read a book by its ID.",
response_model=Book,
status_code=200
)
def read_book(book_id: int, session: Session = Depends(get_session)) -> Book:
    """Retrieve a book by its ID."""
    return book_service.read_book(book_id, session)

#Create Dummy Books
@router.post("/add_books",
summary="Create Dummy Books",
description="Create five sample books in the database.",
response_model=list[Book],
status_code=201
)
def create_dummy_books(session: Session = Depends(get_session)) -> list[Book]:
    """Create five sample books in the database."""
    return book_service.create_dummy_books(session)

# Create a new book
@router.post("/",
summary="Create a New Book",
description="Create a new book in the database.",
response_model=Book,
status_code=201
)
def create_books(book: Book, session: Session = Depends(get_session)) -> Book:
    """Create a new book in the database."""
    return book_service.create_book(book, session)

# Delete a book by ID
@router.delete("/{book_id}",
summary="Delete a Book by ID",
description="Delete a book by its ID.",
response_model=str,
status_code=200
)
def delete_book(book_id: int, session: Session = Depends(get_session)) -> str:
    """Delete a book by its ID."""
    return book_service.delete_book(book_id, session)

# Update a book by ID
@router.put("/{book_id}",
summary="Update a Book by ID",
description="Update a book by its ID.",
response_model=Book,
status_code=200
)
def update_book(book_id: int, updated_book: Book, session: Session = Depends(get_session)) -> Book:
    """Update a book by its ID."""
    return book_service.update_book(book_id, updated_book, session)