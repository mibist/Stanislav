class Car:
    def price_car(self):
        print(f'Цена автомобиля = {self.price}')
    price = 1000000
    def horse_powers(self):
        print(f'Лошадиные силы = {self.HP}')
    HP = 100
class Nissan(Car):
    price = 1500000
    HP = 150

class Kia(Car):
    price = 1800000
    HP = 180

print('Машина стандарт')
car = Car()
car.price_car()
car.horse_powers()

print('Машина НИСАН')
nissan = Nissan()
nissan.price_car()
nissan.horse_powers()

print('Машина КИА')
kia = Kia()
kia.price_car()
kia.horse_powers()