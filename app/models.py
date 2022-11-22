from pydantic import BaseModel


# Item 관련 시작
class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
# Item 관련 끝


# User 관련 시작
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: str | None = None
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
# User 관련 끝

# Token 관련 시작
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
# Token 관련 끝