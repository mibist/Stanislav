# СДЕЛАЛ КАК ПО ЗАДАНИЮ
# import csv
#
# def write_holiday_cities(first_letter):
#     visited = set()
#     want_to_visit = set()
#
#     with open('travel-notes.csv', mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             name, visited_cities, future_cities = row[0], row[1], row[2]
#             if name.startswith(first_letter):
#                 visited.update(visited_cities.split(';'))
#                 want_to_visit.update(future_cities.split(';'))
#
#     never_visited = want_to_visit - visited
#
#     first_city_to_visit = sorted(never_visited)[0] if never_visited else ""
#
#     with open('holiday.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Посетили: " + ", ".join(sorted(visited))])
#         writer.writerow(["Хотят посетить: " + ", ".join(sorted(want_to_visit))])
#         writer.writerow(["Никогда не были в: " + ", ".join(sorted(never_visited))])
#         writer.writerow(["Следующим городом будет: " + first_city_to_visit])
#
# # Пример использования
# write_holiday_cities('L')

# БОЛЕЕ УДОБНЫЙ ВАРИАНТ НА МОЙ ВЗГЛЯД
import csv

def list_available_names():
    names = set()
    with open('travel-notes.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0].strip()
            names.add(name)
    return names

def write_holiday_cities(first_letter_or_name):
    visited = set()
    want_to_visit = set()
    names_matched = set()

    with open('travel-notes.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name, visited_cities, future_cities = row[0], row[1], row[2]
            if name.startswith(first_letter_or_name):
                names_matched.add(name)
                visited.update(visited_cities.split(';'))
                want_to_visit.update(future_cities.split(';'))

    if not names_matched:
        print(f"Нет студентов с именем, начинающимся на '{first_letter_or_name}'")
        return

    never_visited = want_to_visit - visited
    first_city_to_visit = sorted(never_visited)[0] if never_visited else ""

    with open('holiday.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Посетили: " + ", ".join(sorted(visited))])
        writer.writerow(["Хотят посетить: " + ", ".join(sorted(want_to_visit))])
        writer.writerow(["Никогда не были в: " + ", ".join(sorted(never_visited))])
        writer.writerow(["Следующим городом будет: " + first_city_to_visit])

    print("Данные записаны в файл holiday.csv.")

# Основной скрипт для взаимодействия с пользователем
def main():
    print("Доступные имена в файле:")
    names = list_available_names()
    print(", ".join(sorted(names)))

    choice = input("Введите первую букву или полное имя для поиска: ")
    write_holiday_cities(choice)

if __name__ == '__main__':
    main()