from fastapi import Depends, FastAPI

from app.dependencies import get_db
from app.routers import dishes, menus, submenus
from app.db.database import Base, engine

# Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_db)])


app.include_router(dishes.router)
app.include_router(menus.router)
app.include_router(submenus.router)
