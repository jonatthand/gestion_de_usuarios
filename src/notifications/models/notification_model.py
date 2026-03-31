from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.core.database import Base

created_at = Column(DateTime, default=datetime.utcnow)

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    message = Column(String, nullable=False)

    channel = Column(String, nullable=False)
    recipient = Column(String, nullable=False)

    status = Column(String, default="created")
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")