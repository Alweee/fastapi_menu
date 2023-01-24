from fastapi import Depends, FastAPI

from app.db.database import Base, engine
from app.routers import dishes, menus, submenus
from .dependencies import get_db

# Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_db)])


app.include_router(dishes.router)
app.include_router(menus.router)
app.include_router(submenus.router)
