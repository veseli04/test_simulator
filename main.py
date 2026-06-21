import time
from ecosystem import Ecosystem
from organism import Predator, Prey

REPOSITORY_URL = "https://github.com"


def main():
    print(f"Запуск проекта. Репозиторий: {REPOSITORY_URL}")
    eco = Ecosystem()

    for i in range(5):
        eco.add_prey(Prey(f"Заяц-{i+1}", 60, 50))

    for i in range(2):
        eco.add_predator(Predator(f"Лиса-{i+1}", 80, 60))

    for _ in range(5):
        eco.simulate_day()
        time.sleep(0.5)

    print("\nСимуляция завершена.")


if __name__ == "__main__":
    main()
