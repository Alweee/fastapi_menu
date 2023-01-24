from typing import Any, Dict, List

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.crud.crud_menu import (get_menus, get_menu, create_menu,
                                update_menu, remove_menu)
from app.dependencies import get_db
from app.schemas.menu import MenuOut, MenuCreateIn, MenuUpdateIn
from app.utils import add_count_submenus_and_dishes_to_menu

router = APIRouter(prefix='/api/v1/menus')


@router.get(
    '/', response_model=List[MenuOut])
def read_menus(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    db_menus = get_menus(db=db, skip=skip, limit=limit)
    for db_menu in db_menus:
        add_count_submenus_and_dishes_to_menu(db, db_menu)
    return db_menus


@router.get(
    '/{menu_id}', response_model=MenuOut)
def read_menu(menu_id: UUID, db: Session = Depends(get_db)):
    db_menu = get_menu(db=db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail='menu not found')
    return add_count_submenus_and_dishes_to_menu(db, db_menu)


@router.post(
    '/', response_model=MenuOut, status_code=status.HTTP_201_CREATED)
def menu_create(menu: MenuCreateIn, db: Session = Depends(get_db)):
    db_menu = create_menu(db=db, menu=menu)
    return add_count_submenus_and_dishes_to_menu(db, db_menu)


@router.patch(
    '/{menu_id}', response_model=MenuOut)
def menu_update(
    menu_id: UUID, menu: MenuUpdateIn, db: Session = Depends(get_db)
):
    db_menu = get_menu(db=db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail='menu not found')
    updated_db_menu = update_menu(db, menu, db_menu)
    return add_count_submenus_and_dishes_to_menu(db, updated_db_menu)


@router.delete('/{menu_id}', response_model=Dict[str, Any])
def delete_menu(menu_id: UUID, db: Session = Depends(get_db)):
    return remove_menu(db=db, menu_id=menu_id)
