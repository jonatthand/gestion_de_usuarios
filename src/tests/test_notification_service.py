from unittest.mock import MagicMock
from src.notifications.services.notification_service import NotificationService
import pytest
from fastapi import HTTPException


def test_create_notification_success():

    # 1. Mock del repository
    mock_repo = MagicMock()

    mock_notification = MagicMock()
    mock_notification.status = None

    mock_repo.create.return_value = mock_notification

    # 2. Mock del sender
    mock_sender = MagicMock()
    mock_sender.send.return_value = True

    # 3. Mock de DB
    mock_db = MagicMock()

    # 4. Mock de data (lo que viene del request)
    mock_data = MagicMock()
    mock_data.title = "Test"
    mock_data.message = "Hello"
    mock_data.channel = "email"
    mock_data.recipient = "test@mail.com"

    # 5. Crear service con dependencias mockeadas
    service = NotificationService(
        repository=mock_repo,
        sender_service=mock_sender
    )

    # 6. Ejecutar método
    result = service.create_notification(mock_db, mock_data, user_id=1)

    # 7. Verificaciones
    assert result.status == "sent"
    mock_sender.send.assert_called_once_with(mock_notification)

    #--------------------------------- CASO FALLA ----------------------------

def test_create_notification_failed():

    # 1. Mock del repository
    mock_repo = MagicMock()

    mock_notification = MagicMock()
    mock_notification.status = None

    mock_repo.create.return_value = mock_notification

    # 2. Mock del sender
    mock_sender = MagicMock()
    mock_sender.send.return_value = False

    # 3. Mock de DB
    mock_db = MagicMock()

    # 4. Mock de data (lo que viene del request)
    mock_data = MagicMock()
    mock_data.title = "Test"
    mock_data.message = "Hello"
    mock_data.channel = "email"
    mock_data.recipient = "test@mail.com"

    # 5. Crear service con dependencias mockeadas
    service = NotificationService(
        repository=mock_repo,
        sender_service=mock_sender
    )

    # 6. Ejecutar método
    result = service.create_notification(mock_db, mock_data, user_id=1)

    # 7. Verificaciones
    assert result.status == "failed"
    mock_sender.send.assert_called_once_with(mock_notification)

#----------------------------- CASO ERROR ----------------------------

def test_create_notification_error():

    # 1. Mock del repository
    mock_repo = MagicMock()

    mock_notification = MagicMock()
    mock_notification.status = None

    mock_repo.create.return_value = mock_notification

    # 2. Mock del sender
    mock_sender = MagicMock()
    mock_sender.send.side_effect = ValueError("invalid email")

    # 3. Mock de DB
    mock_db = MagicMock()

    # 4. Mock de data (lo que viene del request)
    mock_data = MagicMock()
    mock_data.title = "Test"
    mock_data.message = "Hello"
    mock_data.channel = "email"
    mock_data.recipient = "bad-email"

    service = NotificationService(mock_repo, mock_sender)

    # 👇 ESTA es la forma correcta en pytest
    with pytest.raises(HTTPException) as exc_info:
        service.create_notification(mock_db, mock_data, user_id=1)

    assert exc_info.value.status_code == 400