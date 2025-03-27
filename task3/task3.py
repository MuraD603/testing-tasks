import sys
import json

# Загрузка JSON-файла
def load_f(file_path):    
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при обработке {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

 # Сохранение данных в JSON-файл
def save_json_file(data, file_path):        
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Отчет успешно сохранен: {file_path}")
    except IOError as e:
        print(f"Ошибка записи в {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

def build_values_map(values_data):
    
    return {item['id']: item['value'] for item in values_data.get('values', [])}

def test_values(test_data, values_map):
    if isinstance(test_data, dict):
        test_id = test_data.get('id')
        if test_id in values_map:
            test_data['value'] = values_map[test_id]

        # Обрабатываем все вложенные структуры, кроме id и value
        for key in test_data:
            if key not in {'id', 'value'}:
                test_data[key] = test_values(test_data[key], values_map)

    elif isinstance(test_data, list):
        return [test_values(item, values_map) for item in test_data]

    return test_data

def main():
    
    if len(sys.argv) != 4:
        print("Ошибка: требуется три аргумента.\n"
              "Использование: python task3.py tests.json values.json report.json", file=sys.stderr)
        sys.exit(1)

    tests_path, values_path, report_path = sys.argv[1:4]

    # Загружаем входные файлы
    tests_data = load_f(tests_path)
    values_data = load_f(values_path)

    # Создаем карту значений и заполняем тесты
    values_map = build_values_map(values_data)
    tests_data['tests'] = test_values(tests_data.get('tests', []), values_map)

    # Сохраняем результат
    save_json_file(tests_data, report_path)

if __name__ == "__main__":
    main()
