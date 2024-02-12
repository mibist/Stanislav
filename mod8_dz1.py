def string_to_int(s):
    try:
        return int(s)
    except ValueError as ve:
        print(f"Ошибка при преобразовании строки в число: {ve}")
        return None

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as fnfe:
        print(f"Файл не найден: {fnfe}")
        return None
    except IOError as ioe:
        print(f"Ошибка ввода/вывода при чтении файла: {ioe}")
        return None

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as zde:
        print(f"Ошибка деления на ноль: {zde}")
        return None
    except TypeError as te:
        print(f"Ошибка типа при делении: {te}")
        return None

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError as ie:
        print(f"Индекс вне диапазона: {ie}")
        return None
    except TypeError as te:
        print(f"Ошибка типа при доступе к элементу списка: {te}")
        return None