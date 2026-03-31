import re
from .base_sender import BaseSender


class EmailSender(BaseSender):

    def send(self, notification):

        if not re.match(r"[^@]+@[^@]+\.[^@]+", notification.recipient):        
            raise ValueError("Formato de email inválido")

        print("Generando template de email...")
        print("Enviando email a", notification.recipient)

        return True