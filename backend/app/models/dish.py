from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True)
    price = Column(String)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey('submenus.id'))

    submenu = relationship('Submenu', back_populates='dishes')
