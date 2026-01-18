from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data Model
class Book(BaseModel):
    id: int
    title: str
    author: str

class BookUpdate(BaseModel):
    title: str
    author: str

# In-memory storage
books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
]

# Endpoints

@app.get("/books", response_model=List[Book])
def get_all_books():
    """Get all books"""
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int):
    """Get a specific book by ID"""
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def add_new_book(book: Book):
    """Add a new book"""
    # Check if ID already exists
    for b in books:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    
    new_book = book.dict()
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    """Update a book"""
    for i, book in enumerate(books):
        if book["id"] == book_id:
            updated_book = book.copy()
            updated_book.update(book_update.dict())
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Delete a book"""
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")