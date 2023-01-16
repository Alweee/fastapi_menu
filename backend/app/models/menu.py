from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base
from .submenu import Submenu  # noqa: F401


class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True)

    submenus = relationship('Submenu', back_populates='menu')
