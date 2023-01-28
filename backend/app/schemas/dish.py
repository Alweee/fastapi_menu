from typing import Optional

from uuid import UUID, uuid4

from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: str
    price: str


class DishCreateIn(DishBase):
    ...


class DishUpdateIn(DishBase):
    ...


class DishOut(DishBase):
    id: Optional[UUID] = uuid4()

    class Config:
        orm_mode = True
