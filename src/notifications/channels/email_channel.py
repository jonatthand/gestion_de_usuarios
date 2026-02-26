from .base_channel import BaseChannel
import re
from datetime import datetime

class EmailChannel(BaseChannel):

    def send(self, notification):

        recipient = notification["recipient"]

        # Validar formato
        if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
            raise ValueError("Email inválido")

        # Simular template
        template = f"""
        Asunto: {notification['title']}
        Mensaje: {notification['message']}
        """

        print(f"[EMAIL] Enviado a {recipient} a las {datetime.utcnow()}")

        return {
            "status": "sent",
            "channel": "email"
        }
