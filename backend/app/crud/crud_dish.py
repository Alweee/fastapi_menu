from typing import Any, Dict, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.dish import Dish
from app.schemas.dish import DishCreate, DishUpdate


def get_dishes(
    db: Session, skip: int = 0, limit: int = 100
) -> List[Dish]:
    return db.query(Dish).offset(skip).limit(limit).all()


def get_dish(db: Session, dish_id: int) -> Dish:
    return db.query(Dish).filter(Dish.id == dish_id).first()


def create_dish(db: Session, submenu_id: UUID, dish: DishCreate):
    db_dish = Dish(**dish.dict(), submenu_id=submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def update_dish(db: Session, dish_id: int, dish: DishUpdate) -> Dish:
    db_dish = db.query(Dish).filter(Dish.id == dish_id).first()
    update_data = dish.dict(exclude_unset=True)
    for field in db_dish:
        if field in update_data:
            setattr(db_dish, field, update_data[field])
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def remove_dish(db: Session, dish_id: int) -> Dict[str, Any]:
    db_dish = db.query(Dish).get(dish_id)
    db.delete(db_dish)
    db.commit()
    return {"status": True,
            "message": "The dish has been deleted"}
