from fastapi import FastAPI
from src.core.database import engine, Base
from src.auth.models.user_model import User
from src.notifications.models.notification_model import Notification
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
        title="TAKE HOME CHALLENGE - NOTIFICACIONES", 
        description="API para la gestión de notificaciones con autenticación de usuarios",
        version="1.0.0"
)

origins = [
    "https://frontend-notifications-eta.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

from src.notifications.controllers.notification_router import router as notification_router
from src.auth.routers.auth_router import router as auth_router


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(notification_router, prefix="/notifications", tags=["Notifications"])





