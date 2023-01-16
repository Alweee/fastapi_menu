from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from .dish import Dish


class SubmenuBase(BaseModel):
    title: str
    description: str


class SubmenuCreate(SubmenuBase):
    ...


class SubmenuUpdate(SubmenuBase):
    ...


class Submenu(SubmenuBase):
    id: Optional[UUID] = uuid4()
    menu_id: int
    dishes: list[Dish] = []

    class Config:
        orm_mode = True
