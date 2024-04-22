import json

def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file:
        data = json.load(file)

    employees = data['employees']

    # Приведение ключа к нижнему регистру, но сохранение символьных различий
    sort_type_normalized = sort_type.lower()

    # Проверка наличия ключа в данных
    keys_in_data = {key.lower(): key for employee in employees for key in employee}
    if sort_type_normalized not in keys_in_data:
        raise ValueError('Bad key for sorting')

    original_key = keys_in_data[sort_type_normalized]

    sample_value = next(employee[original_key] for employee in employees if original_key in employee)
    if isinstance(sample_value, str):
        sorted_employees = sorted(employees, key=lambda x: x[original_key])
    else:
        sorted_employees = sorted(employees, key=lambda x: -x[original_key])

    output_filename = f'employees_{sort_type_normalized}_sorted.json'
    with open(output_filename, 'w') as file:
        json.dump({"employees": sorted_employees}, file, indent=4)

    print(f"Данные успешно записаны в файл '{output_filename}'")

try:
    employees_rewrite('lastName')
except ValueError as e:
    print(e)