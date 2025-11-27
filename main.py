from abc import ABC, abstractmethod


class Fighter(ABC):
    def __init__(self, name: str, health: int):
        self.name: str = name
        self.health: int = health

    @abstractmethod
    def attack(self):
        pass
