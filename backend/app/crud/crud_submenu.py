from typing import Any, Dict, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.dish import Dish
from app.models.submenu import Submenu
from app.schemas.submenu import SubmenuCreateIn, SubmenuUpdateIn


def get_count_dishes_for_submenu(db: Session, submenu_id: UUID) -> int:
    return db.query(Dish).filter(Dish.submenu_id == submenu_id).count()


def get_submenus(
    db: Session, skip: int = 0, limit: int = 100
) -> List[Submenu]:
    return db.query(Submenu).offset(skip).limit(limit).all()


def get_submenu(db: Session, submenu_id: int) -> Submenu:
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()


def create_submenu(
    db: Session, menu_id: UUID, submenu: SubmenuCreateIn
) -> Submenu:
    db_submenu = Submenu(**submenu.dict(), menu_id=menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def update_submenu(
    db: Session, submenu: SubmenuUpdateIn, db_submenu: Submenu
) -> Submenu:
    update_data = submenu.dict(exclude_unset=True)
    for field in db_submenu.__dict__:
        if field in update_data:
            setattr(db_submenu, field, update_data[field])
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def remove_submenu(db: Session, submenu_id: int) -> Dict[str, Any]:
    db_submenu = db.query(Submenu).get(submenu_id)
    db.delete(db_submenu)
    db.commit()
    return {"status": True,
            "message": "The submenu has been deleted"}
