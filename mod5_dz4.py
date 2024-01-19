class Building:
    total = 0
    def __init__(self):
        Building.total += 1

building_objects = [Building() for _ in range(40)]

for i, building in enumerate(building_objects, start=1):
    print(f"Building {i}: {building}")


print(f"Total number of buildings: {Building.total}")