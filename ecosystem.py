import random
from organism import Predator, Prey


class Ecosystem:

    def __init__(self):
        self.preys: list[Prey] = []
        self.predators: list[Predator] = []
        self.day = 0

    def add_prey(self, prey: Prey):
        self.preys.append(prey)

    def add_predator(self, predator: Predator):
        self.predators.append(predator)

    def simulate_day(self):
        self.day += 1
        print(f"\n--- День {self.day} ---")

        for prey in self.preys:
            prey.eat()

        for predator in self.predators:
            predator.hunt(self.preys)

        self._update_population()

        print(f"Живых травоядных: {len(self.preys)}")
        print(f"Живых хищников: {len(self.predators)}")

    def _update_population(self):
        for prey in self.preys:
            prey.age_one_day()
        for predator in self.predators:
            predator.age_one_day()

        self.preys = [p for p in self.preys if p.is_alive()]
        self.predators = [p for p in self.predators if p.is_alive()]

        if len(self.preys) > 1 and random.random() < 0.2:
            self.add_prey(Prey(f"Заяц-{random.randint(10, 99)}", 50, 40))
