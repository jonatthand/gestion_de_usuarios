from src.notifications.strategies.sender_factory import SenderFactory

class SenderService:

    def send(self, notification):
        sender = SenderFactory.get_sender(notification.channel)
        return sender.send(notification)