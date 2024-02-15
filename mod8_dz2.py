class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

def generate_exceptions(argument):
    try:
        if argument == 1:
            raise InvalidDataException("Обнаружены неверные данные!")
        elif argument == 2:
            raise ProcessingException("Ошибка во время обработки!")
        else:
            # В данном примере используется обычное исключение ValueError
            raise ValueError("Произошла неизвестная ошибка!")
    except InvalidDataException as e:
        print(f"Поймано исключение InvalidDataException: {e}")
        # Передача обработанного исключения выше по стеку вызовов
        raise
    except ProcessingException as e:
        print(f"Поймано исключение ProcessingException: {e}")
        # Передача обработанного исключения выше по стеку вызовов
        raise
    except Exception as e:
        print(f"Поймано общее исключение: {e}")
        # Передача обработанного исключения выше по стеку вызовов
        raise
    else:
        print("Исключение не произошло.")
    finally:
        print("Блок finally выполнен.")

def main():
    try:
        generate_exceptions(1)
    except InvalidDataException as e:
        print(f"Основная функция поймала InvalidDataException: {e}")
    except ProcessingException as e:
        print(f"Основная функция поймала ProcessingException: {e}")
    except Exception as e:
        print(f"Основная функция поймала общее исключение: {e}")
    else:
        print("В основной функции исключение не произошло.")
    finally:
        print("Основная функция, блок finally выполнен.")

if __name__ == "__main__":
    main()