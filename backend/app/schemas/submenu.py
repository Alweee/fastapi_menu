from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: str


class SubmenuCreateIn(SubmenuBase):
    ...


class SubmenuUpdateIn(SubmenuBase):
    ...


class SubmenuOut(SubmenuBase):
    id: Optional[UUID] = uuid4()
    dishes_count: int

    class Config:
        orm_mode = True
