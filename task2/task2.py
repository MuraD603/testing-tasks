import sys
import math

def read_coordinates(file_path):
    """Чтение центра окружности и радиуса из файла"""
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            if len(lines) < 2:
                raise ValueError("Файл должен содержать минимум 2 строки")
            
            center = tuple(map(float, lines[0].split()))
            radius = float(lines[1])
            
        return center, radius
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")

def read_points(file_path):
    """Чтение координат точек из файла"""
    try:
        with open(file_path, 'r') as file:
            return [tuple(map(float, line.strip().split())) 
                   for line in file if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")

def point_position(center, radius, point):
    """Определение положения точки относительно окружности"""
    distance_squared = (point[0] - center[0])**2 + (point[1] - center[1])**2
    radius_squared = radius**2
    
    if math.isclose(distance_squared, radius_squared, rel_tol=1e-9):
        return 0
    return 1 if distance_squared < radius_squared else 2

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError(
                "Использование: python task2/task2.py <файл_окружности> <файл_точек>\n"
                "Пример: python task2/task2.py circle.txt points.txt\n"
                "python task2/task2.py task2/circle.txt task2/points.txt"
            )
            
        center, radius = read_coordinates(sys.argv[1])
        points = read_points(sys.argv[2])
        
        for point in points:
            print(point_position(center, radius, point))
            
    except Exception as e:
        print(f"Ошибка: {str(e)}", file=sys.stderr)
        sys.exit(1)