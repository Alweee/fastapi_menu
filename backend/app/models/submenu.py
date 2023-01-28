from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class Submenu(Base):
    __tablename__ = 'submenus'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True)
    menu_id = Column(UUID(as_uuid=True), ForeignKey('menus.id'))

    menu = relationship('Menu', back_populates='submenus')
    dishes = relationship(
        'Dish', cascade='all, delete', back_populates='submenu')
