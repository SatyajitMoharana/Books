from sqlmodel import Field, Session, SQLModel, create_engine, select

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str 
    author: str 
    year: int | None =None
    isbn: str | None =None
    available: bool =True
