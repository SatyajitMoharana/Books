from fastapi import APIRouter, Depends
from sqlmodel import Session, select

id=0
def get_id():
    """Generate a unique ID for each book."""
    global id
    id += 1     
    return id

def read_all_books(session: Session) -> list[Book]:
    """Retrieve all books from the database."""
    statement = select(Book)
    results = session.exec(statement)
    return results.all()

def read_book(book_id: int, session: Session) -> Book:
    """Retrieve a book by its ID."""
    statement = select(Book).where(Book.id == book_id)
    book = session.exec(statement).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

def create_dummy_books(session: Session) -> list[Book]:
    """Create five sample books in the database."""
    book1 = Book(id=get_id(), title="Book-1", author="Author -1", year=2021, available=True, isbn="123")
    book2 = Book(id=get_id(), title="Book-2", author="Author -2", year=2020, available=True, isbn="04321")
    session.add(book1)
    session.commit()
    session.add(book2)
    session.commit()
    session.refresh(book1)
    session.refresh(book2)
    return [book1, book2]

def create_book(book: Book, session: Session) -> Book:
    """Create a new book in the database."""
    if book.id is None:
        book.id = get_id()  
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def delete_book(book_id: int, session: Session) -> str:
    """Delete a book from the database by its ID."""
    statement = select(Book).where(Book.id == book_id)
    book = session.exec(statement).first()
    if book:
        session.delete(book)
        session.commit()
        return f"Book with ID {book_id} deleted successfully."
    else:
        return f"Book with ID {book_id} not found."

def update_book(book_id: int, updated_book: Book, session: Session) -> Book:
    """Update a book details by its ID."""
    statement = select(Book).where(Book.id == book_id)
    book = session.exec(statement).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = updated_book.title
    book.author = updated_book.author
    book.year = updated_book.year
    book.available = updated_book.available
    book.isbn = updated_book.isbn
    
    session.add(book)
    session.commit()
    session.refresh(book)
    return book