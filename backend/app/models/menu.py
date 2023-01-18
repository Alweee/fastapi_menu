from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class Menu(Base):
    __tablename__ = 'menus'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True)

    submenus = relationship('Submenu', cascade="all,delete", back_populates='menu')
