import random


class Organism:

    def __init__(self, name: str, health: int, energy: int):
        self.name = name
        self.health = health
        self.energy = energy
        self.age = 0

    def is_alive(self) -> bool:
        return self.health > 0

    def age_one_day(self):
        self.age += 1
        self.energy -= 5
        if self.energy <= 0:
            self.health -= 10


class Prey(Organism):

    def eat(self):
        if self.is_alive():
            if random.random() > 0.3:
                self.energy = min(100, self.energy + 20)
                self.health = min(100, self.health + 5)


class Predator(Organism):

    def hunt(self, prey_list: list[Prey]) -> bool:
        if not self.is_alive() or not prey_list:
            return False

        target = random.choice(prey_list)
        if target.is_alive():
            success_chance = 0.6 if self.energy > 30 else 0.4
            if random.random() < success_chance:
                target.health = 0
                self.energy = min(100, self.energy + 35)
                self.health = min(100, self.health + 10)
                return True

        self.energy -= 10
        return False

