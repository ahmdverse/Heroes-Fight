from abc import ABC, abstractmethod


class Fighter(ABC):
    def __init__(self, name: str, health: int):
        self.name: str = name
        self.health: int = health

    @abstractmethod
    def attack(self, other_fighter: "Fighter"):
        pass


class Hero(Fighter):
    def __init__(self, name: str, health: int, weapon: str):
        super().__init__(name, health)
        self.weapon: str = weapon

    def attack(self, other_fighter: "Fighter"):
        damage = 10
        other_fighter.health -= 10
        print(f"⚔️  {self.name} attacks {other_fighter.name} with {self.weapon}!")
        print(
            f"💥  {other_fighter.name} took {damage} damage. Health is now {other_fighter.health}"
        )
