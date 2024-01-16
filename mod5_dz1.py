class House:
    def __init__(self):
        self.numberOfFloors = 10

    def print_floors(self):
        for floor in range(1, self.numberOfFloors + 1):
            print(f"Текущий этаж равен {floor}")

my_house = House()
my_house.print_floors()