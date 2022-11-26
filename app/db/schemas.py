from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

    def __repr__(self):
        return f"Item(id={self.id!r}, title={self.title!r})"

# 테이블 즉시 생성시 사용
# Base.metadata.create_all(bind=db_sqlite.engine)

# TODO: 테이블 변경시 사용하는 코드도 추가하기
