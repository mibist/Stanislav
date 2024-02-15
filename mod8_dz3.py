import warnings

def divide(a, b):
    if abs(b) < 0.01:
        warnings.warn("Опасность деления на ноль!", UserWarning)

    return a / b

def main():
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("always")
            result = divide(5, 0)
            print("Результат деления:", result)
    except ZeroDivisionError as e:
        print(f"Произошла ошибка деления: {e}")

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = divide(10, 0.005)
            print("Результат деления:", result)
    except ZeroDivisionError as e:
        print(f"Произошла ошибка деления: {e}")

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            result = divide(8, 0.001)
            print("Результат деления:", result)
    except ZeroDivisionError as e:
        print(f"Произошла ошибка деления: {e}")
    except UserWarning as e:
        print(f"Произошло предупреждение: {e}")

if __name__ == "__main__":
    main()