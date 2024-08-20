from pydantic import BaseModel


class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    is_active: bool
    books: list[Book] = []

    class Config:
        orm_mode = True


class SaleBase(BaseModel):
    client_id: int
    bool_id: int

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    name: str
    email: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    purchases: list[Sale] = []

    class Config:
        orm_mode = True