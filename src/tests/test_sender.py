from src.notifications.strategies.email_sender import EmailSender
from src.notifications.strategies.sender_factory import SenderFactory
from src.notifications.strategies.sms_sender import SMSSender
from src.notifications.strategies.push_sender import PushSender
import pytest

#-----------------------------------------------------------------------------------------------
#--------------------------------- SENDER FACTORY ----------------------------------------------
#-----------------------------------------------------------------------------------------------

#--------------------------------- DEVUELVE EMAIL SENDER --------------------------------
def test_sender_factory_email():

    class FakeNotification:
        channel = "email"
        recipient = "test@mail.com"
        message = "Hello"
        title = "Test"

    notification = FakeNotification()

    result = SenderFactory.send(notification)

    assert result is True


def test_sender_factory_invalid_channel():
    class FakeNotification:
        channel = "fax"

    notification = FakeNotification()

    with pytest.raises(ValueError):
        SenderFactory.send(notification)

#-----------------------------------------------------------------------------------------------
#--------------------------------- TESTEA EMAIL SENDER -----------------------------------------
#-----------------------------------------------------------------------------------------------

def test_email_sender_success():

    class FakeNotification:
        recipient = "test@mail.com"
        message = "Hello"
        title = "Test"

    sender = EmailSender()

    result = sender.send(FakeNotification())

    assert result is True



def test_email_sender_invalid_email():

    class FakeNotification:
        recipient = "invalid-email"
        message = "Hello"
        title = "Test"

    sender = EmailSender()

    with pytest.raises(ValueError):
        sender.send(FakeNotification())


#-----------------------------------------------------------------------------------------------
#--------------------------------- TESTEAR SMS SENDER ------------------------------------------
#-----------------------------------------------------------------------------------------------


def test_sms_sender_success():

    class FakeNotification:
        recipient = "123456789"
        message = "Hello"
        title = "Test"

    sender = SMSSender()

    result = sender.send(FakeNotification())

    assert result is True


def test_sms_sender_long_message():

    class FakeNotification:
        recipient = "123456789"
        message = "x" * 200  # 👈 más de 160 caracteres
        title = "Test"

    sender = SMSSender()

    with pytest.raises(ValueError):
        sender.send(FakeNotification())

#-----------------------------------------------------------------------------------------------
#--------------------------------- TESTEAR PUSH SENDER -----------------------------------------
#-----------------------------------------------------------------------------------------------


def test_push_sender_success():

    class FakeNotification:
        recipient = "device_token"
        message = "Hello"
        title = "Test"

    sender = PushSender()

    result = sender.send(FakeNotification())

    assert result is True


def test_push_sender_invalid_token():

    class FakeNotification:
        recipient = ""  # 👈 inválido
        message = "Hello"
        title = "Test"

    sender = PushSender()

    with pytest.raises(ValueError):
        sender.send(FakeNotification())