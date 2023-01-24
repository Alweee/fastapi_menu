from typing import Any, Dict, List

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.menu import Menu
from app.models.submenu import Submenu
from app.schemas.menu import MenuCreateIn, MenuUpdateIn


def get_submenus_count_for_menu(db: Session, menu_id: UUID) -> int:
    return db.query(Submenu).filter(menu_id == Submenu.menu_id).count()


def get_dishes_count_for_menu(db: Session, menu_id: UUID) -> int:
    dishes_count = 0
    for submenu in db.query(Submenu).filter(menu_id == Submenu.menu_id).all():
        dishes_count += len(submenu.dishes)
    return dishes_count


def get_menus(db: Session, skip: int = 0, limit: int = 100) -> List[Menu]:
    return db.query(Menu).offset(skip).limit(limit).all()


def get_menu(db: Session, menu_id: UUID) -> Menu:
    return db.query(Menu).filter(menu_id == menu_id).first()


def create_menu(db: Session, menu: MenuCreateIn) -> Menu:
    db_menu = Menu(**menu.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def update_menu(db: Session, menu: MenuUpdateIn, db_menu: Menu) -> Menu:
    update_data = menu.dict(exclude_unset=True)
    for field in db_menu.__dict__:
        if field in update_data:
            setattr(db_menu, field, update_data[field])
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def remove_menu(db: Session, menu_id: UUID) -> Dict[str, Any]:
    db_menu = db.query(Menu).get(menu_id)
    db.delete(db_menu)
    db.commit()
    return {"status": True,
            "message": "The menu has been deleted"}
