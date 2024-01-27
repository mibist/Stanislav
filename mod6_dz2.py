class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car:
    def __init__(self):
        price = 1000000
    def horse_powers(self):
        print(f'Лошадиные силы = {self.HP}')
    HP = 100

class Nissan(Vehicle, Car):
    def __init__(self):
        super().__init__()

        self.vehicle_type = 'хэчбэк'
        self.price = 1500000
        self.HP = 150


print('Машина НИСАН')
nissan = Nissan()
print('Цена автомобиля =', nissan.price)
print('Класс автомобиля', nissan.vehicle_type)
nissan.horse_powers()