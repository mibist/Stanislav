import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.days = 0
        self.remaining_enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.remaining_enemies > 0:
            self.days += 1
            daily_defense = min(self.skill, self.remaining_enemies)
            self.remaining_enemies -= daily_defense
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.remaining_enemies} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней!")

if __name__ == "__main__":
    knight1 = Knight("Sir Lancelot", 10)
    knight2 = Knight("Sir Galahad", 20)

    knight1.start()
    knight2.start()

    knight1.join()
    knight2.join()

    print("Все битвы закончились!")