from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выводит результат вычеслений."""
    res = calculate_square_root(your_number)
# Спросить о ненормальном расположении print, не хватает отступов
# но по другому не работает!!!
    print('Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {res}')


print(message)
calc(25.5)
