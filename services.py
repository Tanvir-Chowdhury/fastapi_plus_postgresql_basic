from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def create__book(db: Session, data: BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh()
    return book_instance

def get_books(db: Session):
    db.query(Book).all()