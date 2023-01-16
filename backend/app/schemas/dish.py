from typing import Optional

from uuid import UUID, uuid4

from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: str
    price: str


class DishCreate(DishBase):
    ...


class DishUpdate(DishBase):
    ...


class Dish(DishBase):
    id: Optional[UUID] = uuid4()
    submenu_id: int

    class Config:
        orm_mode = True
