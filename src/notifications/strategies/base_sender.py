from abc import ABC, abstractmethod


class BaseSender(ABC):

    @abstractmethod
    def send(self, notification):
        pass