from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.crud.crud_submenu import (get_submenus, get_submenu, create_submenu,
                                   update_submenu, remove_submenu)
from app.dependencies import get_db
from app.schemas.submenu import SubmenuOut, SubmenuCreateIn, SubmenuUpdateIn
from app.utils import add_count_dishes_to_submenu

router = APIRouter(prefix='/api/v1/menus',)


@router.get('/{menu_id}/submenus/', response_model=List[SubmenuOut])
def read_submenus(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    db_submenus = get_submenus(db=db, skip=skip, limit=limit)
    for db_submenu in db_submenus:
        add_count_dishes_to_submenu(db, db_submenu)
    return db_submenus


@router.get('/{menu_id}/submenus/{submenu_id}', response_model=SubmenuOut)
def read_submenu(submenu_id: UUID, db: Session = Depends(get_db)):
    db_submenu = get_submenu(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail='submenu not found')
    return add_count_dishes_to_submenu(db, db_submenu)


@router.post(
    '/{menu_id}/submenus/',
    response_model=SubmenuOut, status_code=status.HTTP_201_CREATED)
def submenu_create(
    menu_id: UUID, submenu: SubmenuCreateIn, db: Session = Depends(get_db)
):
    db_submenu = create_submenu(db=db, menu_id=menu_id, submenu=submenu)
    return add_count_dishes_to_submenu(db, db_submenu)


@router.patch(
    '/{menu_id}/submenus/{submenu_id}', response_model=SubmenuOut)
def submenu_update(
    submenu_id: UUID, submenu: SubmenuUpdateIn,
    db: Session = Depends(get_db)
):
    db_submenu = get_submenu(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail='submenu not found')
    updated_db_submenu = update_submenu(
        db=db, submenu=submenu, db_submenu=db_submenu)
    return add_count_dishes_to_submenu(db, updated_db_submenu)


@router.delete(
    '/{menu_id}/submenus/{submenu_id}', response_model=Dict[str, Any])
def delete_submenu(submenu_id: UUID, db: Session = Depends(get_db)):
    return remove_submenu(db=db, submenu_id=submenu_id)
