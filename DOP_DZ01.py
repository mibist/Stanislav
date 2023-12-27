# Предположим, что данные хранятся в файле с именем 'logs.txt'
file_name = 'logs.txt'

# Создаем пустой список для хранения данных о посещениях
visits_data = []

# Чтение файла и разделение строк на время посещения и URL страницы
with open(file_name, 'r') as file:
    for line in file:
        # Разделение строки на время и URL страницы и добавление в список
        time_visited, url = line.strip().split(' : ')
        visits_data.append((time_visited, url))
        #line.strip(): Удаляет пробельные символы и символы новой строки из строки line.Это помогает избавиться от
        # лишних пробелов в начале или конце строки, что может возникнуть при чтении из файла.
        # Проверка для первых нескольких строк, чтобы убедиться, что данные корректно считываются
        #print(f'Время посещения:', (time_visited), 'URL страницы:',  (url))
# Создаем словарь для подсчета посещений страниц
page_visits = {}

# Подсчет количества посещений каждой страницы
for _, url in visits_data:
    if url in page_visits:
        page_visits[url] += 1
    else:
        page_visits[url] = 1

# Вывод словаря для проверки
#print('Словарь с количеством посещений каждой страницы:', page_visits)

# Находим страницу с наибольшим количеством посещений
most_visited_page = max(page_visits, key=page_visits.get)
visits_count = page_visits[most_visited_page]

print(f'Самая посещаемая страница:', {most_visited_page})
print(f'Количество посещений:', {visits_count})