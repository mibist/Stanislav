class Building:
    def __init__(self, number_of_floors, building_type):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False

building1 = Building(1, "Магазин")
building2 = Building(1, "Магазин")
building3 = Building(2, "Офис")

print(building1 == building2)  # Вывод: True
print(building1 == building3)  # Вывод: False