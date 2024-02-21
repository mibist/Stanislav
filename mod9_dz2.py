# Задача 1: Фабрика функций
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract

add_function = create_operation("add")
print(add_function(3, 4))

subtract_function = create_operation("subtract")
print(subtract_function(8, 5))

# Задача 2: Лямбда-Функции

square_lambda = lambda x: x ** 2
print(square_lambda(4))

# Аналогичная функция с использованием def
def square_def(x):
    return x ** 2
print(square_def(4))

# Задача 3: Вызываемые Объекты

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

rectangle = Rect(2, 4)
print("Стороны:", rectangle.a, ",", rectangle.b)
print("Площадь:", rectangle())