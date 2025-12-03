from sqlmodel import Field, Session, SQLModel, create_engine, select

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)

def create_db_and_tables():
  from src.db.models import Book
  SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
