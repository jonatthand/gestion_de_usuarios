from fastapi import FastAPI
from src.auth.routers.auth_router import router as auth_router
from src.core.database import engine, Base
from src.auth.models.user_model import User
from src.notifications.models.notification_model import Notification
from src.notifications.controllers.notification_router import router as notification_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
        title="TAKE HOME CHALLENGE - NOTIFICACIONES", 
        description="API para la gestión de notificaciones con autenticación de usuarios",
        version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontend-notifications-eta.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notification_router, prefix="/notifications", tags=["Notifications"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])





