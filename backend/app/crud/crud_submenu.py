from typing import Any, Dict, List

from sqlalchemy.orm import Session

from app.models.submenu import Submenu
from app.schemas.submenu import SubmenuCreate, SubmenuUpdate


def get_submenus(
    db: Session, skip: int = 0, limit: int = 100
) -> List[Submenu]:
    return db.query(Submenu).offset(skip).limit(limit).all()


def get_submenu(db: Session, submenu_id: int) -> Submenu:
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()


def create_submenu(db: Session, submenu: SubmenuCreate):
    db_submenu = Submenu(**submenu.dict())
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def update_submenu(
    db: Session, submenu_id: int, submenu: SubmenuUpdate
) -> Submenu:
    db_submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    update_data = submenu.dict(exclude_unset=True)
    for field in db_submenu:
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
