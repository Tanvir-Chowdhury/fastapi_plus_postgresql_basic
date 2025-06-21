from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from db import get_db, engine 
from sqlalchemy.orm import Session

app = FastAPI()

@app.get('/books/', response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return services.get_books(db)

@app.get('/books/{book_id}', response_model=list[schemas.Book])
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = services.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    return book

@app.post('/books/', response_model=list[schemas.Book])
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create__book(db, book)


@app.put("/books/{book_id}", response_model=list[schemas.Book])
def update_book(  book: schemas.BookCreate ,book_id: int, db: Session = Depends(get_db)):
    db_update = services.update_book(db, book, book_id)
    if not db_update:
        raise HTTPException(status_code=404, detail='Book not found')
    return db_update

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_delete = services.delete_book(db, book_id)
    if not db_delete:
        raise HTTPException(status_code=404, detail='Book not found')
    return db_delete