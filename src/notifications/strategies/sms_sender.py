from .base_sender import BaseSender


class SMSSender(BaseSender):

    def send(self, notification):

        if len(notification.message) > 160:
            raise ValueError("SMS excede 160 caracteres")

        print("Enviando SMS a", notification.recipient)

        return "sent"