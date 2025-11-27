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


class Enemy(Fighter):
    def __init__(self, name: str, health: int, damage_power: int):
        super().__init__(name, health)
        self.damage_power: int = damage_power

    def attack(self, other_fighter: "Fighter"):
        other_fighter.health -= self.damage_power
        print(f"👹 {self.name} bites {other_fighter.name} aggressively!")
        print(
            f"🩸 {other_fighter.name} took {self.damage_power} damage. Health is now {other_fighter.health}"
        )


# --------------------------------
# Game
# --------------------------------

if __name__ == "__main__":
    my_hero = Hero("Super Ahmed", 100, "Slipper 🩴")

    my_enemy = Enemy("Angry Biso", 50, 15)

    print("🚨 --- BATTLE STARTED --- 🚨")

    while my_hero.health > 0 and my_enemy.health > 0:

        my_hero.attack(my_enemy)

        if my_enemy.health <= 0:
            print(f"\n🏆 VICTORY! {my_enemy.name} is defeated!")
            break

        print("-----------------------")

        my_enemy.attack(my_hero)

        if my_hero.health <= 0:
            print(f"\n💀 GAME OVER! {my_hero.name} died...")
            break

        print("\nNext Round...")
