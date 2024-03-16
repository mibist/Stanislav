import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# requests - для работы с HTTP-запросами и API.
# Запрашиваем данные с API
response = requests.get("https://api.example.com/data")
data = response.json()

# Выводим данные в консоль
print(data)


# pandas - для работы с данными в формате таблиц.
# Считываем данные из файла
data = pd.read_csv("data.csv")

# Выполняем анализ данных
summary = data.describe()

# Выводим результаты
print(summary)

# numpy - для работы с массивами чисел и выполнения математических операций.
# Создаем массив чисел
arr = np.array([1, 2, 3, 4, 5])

# Выполняем математические операции
mean = np.mean(arr)
sum_val = np.sum(arr)

# Выводим результаты
print("Среднее значение:", mean)
print("Сумма значений:", sum_val)


# matplotlib - для визуализации данных.
# Данные для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Строим график
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Пример графика")
plt.show()


# Pillow - для обработки изображений.
# Открываем изображение
img = Image.open("image.jpg")

# Изменяем размер изображения
resized_img = img.resize((100, 100))

# Применяем эффекты (например, поворот)
rotated_img = img.rotate(45)

# Сохраняем изображения в другом формате
resized_img.save("resized_image.jpg")
rotated_img.save("rotated_image.jpg")