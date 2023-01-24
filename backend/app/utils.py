from sqlalchemy.orm import Session

from app.crud.crud_menu import (get_submenus_count_for_menu,
                                get_dishes_count_for_menu)
from app.crud.crud_submenu import get_count_dishes_for_submenu
from app.models.menu import Menu
from app.models.submenu import Submenu


def add_count_submenus_and_dishes_to_menu(db: Session, db_menu: Menu) -> Menu:
    db_menu_dict = db_menu.__dict__
    db_menu_dict.update(
        {'submenus_count': get_submenus_count_for_menu(db, db_menu.id),
         'dishes_count': get_dishes_count_for_menu(db, db_menu.id)})
    return db_menu


def add_count_dishes_to_submenu(db: Session, db_submenu: Submenu) -> Submenu:
    db_submenu_dict = db_submenu.__dict__
    db_submenu_dict.update(
        {'dishes_count': get_count_dishes_for_submenu(db, db_submenu.id)})
    return db_submenu
