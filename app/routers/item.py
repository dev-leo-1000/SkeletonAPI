from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import schemas
from app.db.database import db_sqlite

router = APIRouter(prefix="/items")


@router.get("/")
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(db_sqlite.session)):
        items = db.query(schemas.Item).offset(skip).limit(limit).all()
        return items


