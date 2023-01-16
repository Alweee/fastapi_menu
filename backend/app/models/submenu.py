from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base
from .dish import Dish  # noqa: F401
from .menu import Menu  # noqa: F401


class Submenu(Base):
    __tablename__ = 'submenus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True)
    menu_id = Column(Integer, ForeignKey('menus.id'))

    menu = relationship('Menu', back_populates='submenus')
    dishes = relationship('Dish', back_populates='submenu')
