from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.crud.crud_menu import (get_menus, get_menu, create_menu, update_menu,
                                remove_menu)
from app.dependencies import get_db
from app.schemas.menu import MenuOut, MenuCreate, MenuUpdate
from app.models.menu import Menu as db_Menu


router = APIRouter(prefix='/api/v1/menus')


@router.get(
    '/', response_model=List[MenuOut])
def read_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    menus = get_menus(db=db, skip=skip, limit=limit)
    return menus


@router.get(
    '/{menu_id}', response_model=MenuOut)
def read_menu(menu_id: UUID, db: Session = Depends(get_db)):
    db_menu = get_menu(db=db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail='menu not found')
    dishes_count = 0
    for submenu in db_menu.submenus:
        dishes_count += len(submenu.dishes)
    return {'id': menu_id, 'title': db_menu.title,
            'description': db_menu.description,
            'submenus_count': len(db_menu.submenus),
            'dishes_count': dishes_count}


@router.post(
    '/', response_model=MenuOut, status_code=status.HTTP_201_CREATED)
def menu_create(menu: MenuCreate, db: Session = Depends(get_db)):
    db_menu = create_menu(db=db, menu=menu)
    return db_menu


@router.patch(
    '/{menu_id}', response_model=MenuOut)
def menu_update(
    menu_id: UUID, menu: MenuUpdate, db: Session = Depends(get_db)
):
    db_menu = get_menu(db=db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail='menu not found')
    return update_menu(db=db, menu_id=menu_id, menu=menu)


@router.delete('/{menu_id}', response_model=Dict[str, Any])
def delete_menu(menu_id: UUID, db: Session = Depends(get_db)):
    return remove_menu(db=db, menu_id=menu_id)
