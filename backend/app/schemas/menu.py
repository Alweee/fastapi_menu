from uuid import UUID, uuid4

from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str


class MenuCreateIn(MenuBase):
    ...


class MenuUpdateIn(MenuBase):
    ...


class MenuOut(MenuBase):
    id: UUID = uuid4()
    submenus_count: int
    dishes_count: int

    class Config:
        orm_mode = True
