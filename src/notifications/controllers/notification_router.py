from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.auth.dependencies import get_current_user
from src.notifications.schemas.notification_schema import NotificationCreate
from src.notifications.services.notification_service import NotificationService
from src.notifications.services.sender_service import SenderService
from src.notifications.repositories.notification_repository import NotificationRepository
from src.notifications.schemas.notification_schema import NotificationUpdate, NotificationResponse


router = APIRouter(tags=["Notifications"])

notification_service = NotificationService(
    repository=NotificationRepository,
    sender_service=SenderService
)


@router.post("/", response_model=NotificationResponse)
def create_notification(
    notification_data: NotificationCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    notification = notification_service.create_notification(
        db,
        notification_data,
        current_user.id
    )

    return notification

@router.get("/")
def get_my_notifications(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    notifications = NotificationRepository.get_by_user(
        db,
        current_user.id
    )

    return notifications

@router.get("/{notification_id}")
def get_notification_by_id(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    notification = NotificationRepository.get_by_id(
        db,
        notification_id
    )

    if not notification:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")

    if notification.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="No autorizado")

    return notification

@router.patch("/{notification_id}")
def update_notification(
    notification_id: int,
    data: NotificationUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    notification = NotificationRepository.get_by_id(db, notification_id)

    if not notification:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")

    if notification.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="No autorizado")

    updated = NotificationRepository.update(db, notification, data)

    return updated

@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    notification = NotificationRepository.get_by_id(db, notification_id)

    if not notification:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")

    if notification.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="No autorizado")

    NotificationRepository.delete(db, notification)

    return {"message": "Notificación eliminada"}