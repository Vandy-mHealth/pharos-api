import os

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.core.config import settings
from app.db import Landmark, Network, Photo, User, db, db_state_default
from app.routers import (landmark_router, network_router, photo_router,
                         user_router)

stage = os.environ.get('STAGE', None)

openapi_prefix = f"/{stage}" if stage else "/"
​

db.connect()
db.create_tables([User, Landmark, Network, Photo])
db.close()


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME, openapi_prefix=openapi_prefix)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


@app.get("/")
def hello():
    return {"message": "hello from Pharos API"}


app.include_router(
    user_router,
    prefix="/user",
    tags=["authentication and user-related queries"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    landmark_router,
    prefix="/landmark",
    tags=["landmark and user-related queries"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    network_router,
    prefix="/network",
    tags=["network measurement related queries"],
    dependencies=[Depends(get_db)],
)

app.include_router(
    photo_router,
    prefix="/photo",
    tags=["photo related queries"],
    dependencies=[Depends(get_db)],
)


handler = Mangum(app)
