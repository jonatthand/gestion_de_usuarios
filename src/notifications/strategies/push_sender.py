from .base_sender import BaseSender


class PushSender(BaseSender):

    def send(self, notification):

        if len(notification.recipient) < 10:
            raise ValueError("Token de dispositivo inválido")

        print("Formateando payload push...")
        print("Enviando notificación push")

        return "sent"