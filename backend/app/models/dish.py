from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base
from .submenu import Submenu  # noqa: F401


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True)
    price = Column(String)
    submenu_id = Column(Integer, ForeignKey('submenus.id'))

    submenu = relationship('Submenu', back_populates='dishes')
