from typing import Any, Dict, List

from sqlalchemy.orm import Session

from app.models.menu import Menu
from app.schemas.menu import MenuCreate, MenuUpdate


def get_menus(db: Session, skip: int = 0, limit: int = 100) -> List[Menu]:
    return db.query(Menu).offset(skip).limit(limit).all()


def get_menu(db: Session, menu_id: int) -> Menu:
    return db.query(Menu).filter(Menu.id == menu_id).first()


def create_menu(db: Session, menu: MenuCreate):
    db_menu = Menu(**menu.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def update_menu(db: Session, menu_id: int, menu: MenuUpdate) -> Menu:
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    update_data = menu.dict(exclude_unset=True)
    for field in db_menu:
        if field in update_data:
            setattr(db_menu, field, update_data[field])
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def remove_menu(db: Session, menu_id: int) -> Dict[str, Any]:
    db_menu = db.query(Menu).get(menu_id)
    db.delete(db_menu)
    db.commit()
    return {"status": True,
            "message": "The menu has been deleted"}
