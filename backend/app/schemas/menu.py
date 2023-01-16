from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from .submenu import Submenu


class MenuBase(BaseModel):
    title: str
    description: str


class MenuCreate(MenuBase):
    ...


class MenuUpdate(MenuBase):
    ...


class Menu(MenuBase):
    id: Optional[UUID] = uuid4()
    submenus: list[Submenu] = []

    class Config:
        orm_mode = True
