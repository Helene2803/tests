# Впишите ваше решение в функции discriminant и solution

def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    # Ваш алгоритм
    x = 0
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        return 'корней нет'

if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))  