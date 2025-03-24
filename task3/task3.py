import sys
import json

def load_json_file(file_path):
    """Загрузка JSON файла с обработкой ошибок"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: файл {file_path} содержит некорректный JSON", file=sys.stderr)
        sys.exit(1)

def save_json_file(data, file_path):
    """Сохранение данных в JSON файл"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except IOError:
        print(f"Ошибка: невозможно записать в файл {file_path}", file=sys.stderr)
        sys.exit(1)

def build_values_map(values_data):
    """Создает словарь {id: value} из данных values.json"""
    return {item['id']: item['value'] for item in values_data['values']}

def fill_test_values(test_structure, values_map):
    """Рекурсивно заполняет значения в структуре теста"""
    if isinstance(test_structure, dict):
        # Заполняем значение для текущего теста
        if 'id' in test_structure:
            test_id = test_structure['id']
            if test_id in values_map:
                test_structure['value'] = values_map[test_id]
        
        # Рекурсивно обрабатываем вложенные элементы
        for key in test_structure:
            if key != 'id' and key != 'value':  # Пропускаем уже обработанные поля
                test_structure[key] = fill_test_values(test_structure[key], values_map)
    
    elif isinstance(test_structure, list):
        # Обрабатываем список тестов
        for i in range(len(test_structure)):
            test_structure[i] = fill_test_values(test_structure[i], values_map)
    
    return test_structure

def main():
    if len(sys.argv) != 4:
        print("Использование: python task3.py tests.json values.json report.json", file=sys.stderr)
        sys.exit(1)

    tests_file, values_file, report_file = sys.argv[1], sys.argv[2], sys.argv[3]

    # Загрузка данных
    tests_data = load_json_file(tests_file)
    values_data = load_json_file(values_file)

    # Создание словаря значений
    values_map = build_values_map(values_data)

    # Заполнение значений в структуре тестов
    report_data = {'tests': fill_test_values(tests_data['tests'], values_map)}

    # Сохранение отчета
    save_json_file(report_data, report_file)
    print(f"Отчет успешно сохранен в {report_file}")

if __name__ == "__main__":
    main()