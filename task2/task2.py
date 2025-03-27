import sys
import math

def load_circle(file_path):
    try:
        with open(file_path, 'r') as file:
            center_x, center_y = map(float, file.readline().split())
            radius = float(file.readline())
        return (center_x, center_y), radius
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("Ошибка: некорректные данные в файле окружности", file=sys.stderr)
        sys.exit(1)

def load_points(file_path):
    try:
        with open(file_path, 'r') as file:
            return [tuple(map(float, line.split())) for line in file]
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("Ошибка: некорректные данные в файле точек", file=sys.stderr)
        sys.exit(1)

def get_point_location(center, radius, point):
    distance_squared = (point[0] - center[0])**2 + (point[1] - center[1])**2
    radius_squared = radius**2
    if math.isclose(distance_squared, radius_squared, rel_tol=1e-9):
        return 0
    return 1 if distance_squared < radius_squared else 2

def main():
    if len(sys.argv) != 3:
        print("Использование: python task.py circle.txt points.txt", file=sys.stderr)
        sys.exit(1)
    
    center, radius = load_circle(sys.argv[1])
    points = load_points(sys.argv[2])
    
    for point in points:
        sys.stdout.write(f"{get_point_location(center, radius, point)}\n")

if __name__ == "__main__":
    main()
