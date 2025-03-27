import sys

def main():
    if len(sys.argv) != 3:
        print("Ошибка: требуется 2 аргумента — n и m")
        print("Пример: python task.py 5 4")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        
        if n <= 0 or m <= 0:
            print("Ошибка: n и m должны быть положительными числами.")
            sys.exit(1)
        
        print(circular_path(n, m))
    except ValueError:
        print("Ошибка: Введите целые числа.")
        sys.exit(1)

def circular_path(n, m):
    arr = list(range(1, n + 1))
    path = []
    current = 0
    
    visited = set()
    
    while current not in visited:
        path.append(str(arr[current]))
        visited.add(current)
        current = (current + m - 1) % n
    
    return ''.join(path)


if __name__ == "__main__":
    main()

