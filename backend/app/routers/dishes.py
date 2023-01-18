from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.crud.crud_dish import (get_dishes, get_dish, create_dish, update_dish,
                                remove_dish)
from app.dependencies import get_db
from app.schemas.dish import Dish, DishCreate, DishUpdate

router = APIRouter(prefix='/api/v1/menus',)


@router.get(
    '/{menu_id}/submenus/{submenu_id}/dishes/',
    response_model=List[Dish])
def read_dishes(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    dishes = get_dishes(db=db, skip=skip, limit=limit)
    return dishes


@router.get(
    '/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}',
    response_model=Dish)
def read_dish(dish_id: int, db: Session = Depends(get_db)):
    db_dish = get_dish(db=db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail='dish not found')
    return db_dish


@router.post(
    '/{menu_id}/submenus/{submenu_id}/dishes/',
    response_model=Dish, status_code=status.HTTP_201_CREATED)
def dish_create(submenu_id: UUID, dish: DishCreate, db: Session = Depends(get_db)):
    return create_dish(db=db, submenu_id=submenu_id, dish=dish)


@router.patch(
    '/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}',
    response_model=Dish)
def dish_update(
    dish_id: int, dish: DishUpdate,
    db: Session = Depends(get_db)
):
    db_dish = get_dish(db=db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail='dish not found')
    return update_dish(db=db, dish_id=dish_id, dish=dish)


@router.delete(
    '/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}',
    response_model=Dict[str, Any])
def delete_dish(dish_id: int, db: Session = Depends(get_db)):
    return remove_dish(db=db, dish_id=dish_id)
