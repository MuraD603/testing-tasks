import sys

def circular_path(n, m):
    arr = list(range(1, n + 1))
    path = []
    current = 0
    
    while True:
        path.append(str(arr[current]))
        current = (current + m - 1) % n
        if current == 0:
            break
    return ''.join(path)

if __name__ == "__main__":
    # Проверка
    if len(sys.argv) != 3:
        print("Ошибка: требуется 2 аргумента — n и m")
        print("Пример: python task1/task1.py 4 3")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Ошибка: аргументы должны быть целыми числами")
        sys.exit(1)
    
    print(circular_path(n, m))