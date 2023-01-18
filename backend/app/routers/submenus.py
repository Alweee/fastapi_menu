from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.crud.crud_submenu import (get_submenus, get_submenu, create_submenu,
                                   update_submenu, remove_submenu)
from app.dependencies import get_db
from app.schemas.submenu import Submenu, SubmenuCreate, SubmenuUpdate

router = APIRouter(prefix='/api/v1/menus',)


@router.get('/{menu_id}/submenus/', response_model=List[Submenu])
def read_submenus(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    submenus = get_submenus(db=db, skip=skip, limit=limit)
    return submenus


@router.get('/{menu_id}/submenus/{submenu_id}', response_model=Submenu)
def read_submenu(submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = get_submenu(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail='submenu not found')
    return db_submenu


@router.post(
    '/{menu_id}/submenus/',
    response_model=Submenu, status_code=status.HTTP_201_CREATED)
def submenu_create(
    menu_id: UUID, submenu: SubmenuCreate, db: Session = Depends(get_db)
):
    return create_submenu(db=db, menu_id=menu_id, submenu=submenu)


@router.patch(
    '/{menu_id}/submenus/{submenu_id}', response_model=Submenu)
def submenu_update(
    submenu_id: int, submenu: SubmenuUpdate,
    db: Session = Depends(get_db)
):
    db_submenu = get_submenu(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail='submenu not found')
    return update_submenu(db=db, submenu_id=submenu_id, submenu=submenu)


@router.delete(
    '/{menu_id}/submenus/{submenu_id}', response_model=Dict[str, Any])
def delete_submenu(submenu_id: int, db: Session = Depends(get_db)):
    return remove_submenu(db=db, submenu_id=submenu_id)
