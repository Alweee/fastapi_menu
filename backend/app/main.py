from typing import List

from fastapi import Depends, FastAPI, Httpexception, status

from sqlalchemy.orm import Session

from app import crud, models, schemas
from .db.database import SessionLocal, engine


app = FastAPI()


@app.get('/api/v1/menus/', response_model=list[Menu])
def read_menus(menu_id: int):
    return {'menu_id': menu_id}


@app.get('/api/v1/menus/{menu_id}', response_model=Menu)
def read_menu(menu_id: int):
    return {'menu_id': menu_id}


@app.post('/api/v1/menus', response_model=Menu,
          status_code=status.HTTP_201_CREATED)
def create_menu(menu: MenuCreate):
    return Menu


@app.patch('api/v1/menus/{menu_id}', response_model=Menu)
def change_menu(menu_id: int, menu: MenuUpdate):
    return Menu


@app.delete('api/v1/menus/{menu_id}')
def delete_menu(menu_id: int):
    return {'status': True,
            'message': 'The menu has been deleted'}
