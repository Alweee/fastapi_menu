from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from app.schemas.submenu import Submenu


class MenuBase(BaseModel):
    title: str
    description: str


class MenuCreate(MenuBase):
    ...


class MenuUpdate(MenuBase):
    ...


class MenuOut(MenuBase):
    id: Optional[UUID] = uuid4()
    submenus_count: int
    dishes_count: int

    class Config:
        orm_mode = True
