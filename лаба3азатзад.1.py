import math


def calculate_y(x):
    """
    Функция для вычисления Y по графику (Вариант 3).
    """
    if x < -7:
        # 1. Нижняя полуокружность, центр (-7, 0), R=2
        return -math.sqrt(4 - (x + 7) ** 2)
    elif -7 <= x < -5:
        # 2. Верхняя полуокружность, центр (-5, 0), R=2
        return math.sqrt(4 - (x + 5) ** 2)
    elif -5 <= x < -4:
        # 3. Горизонтальная полка
        return 2
    elif -4 <= x < 0:
        # 4. Наклонная прямая y = -0.5x
        return -0.5 * x
    elif 0 <= x < math.pi / 2:
        # 5. Первая полуволна синуса (горб вверх)
        return math.sin(x)
    elif math.pi / 2 <= x <= math.pi:
        # 6. Вторая полуволна (ямка вниз!)
        # Используем -sin(x), чтобы график ушел вниз
        return -math.sin(x)
    else:  # x > math.pi
        # 7. Прямая под углом 45 градусов (y = x - pi)
        return x - math.pi


def main():
    print("Лабораторная работа №3. Задание 1 (Вариант 3)")
    print("Вычисление значений функции в виде таблицы\n")

    try:
        x_start = float(input("Введите Xнач (начало интервала): "))
        x_end = float(input("Введите Xкон (конец интервала): "))
        dx = float(input("Введите dx (шаг): "))

        if dx <= 0:
            print("Ошибка: Шаг (dx) должен быть положительным.")
            return
        if x_start > x_end:
            print("Ошибка: Начало интервала больше конца.")
            return

    except ValueError:
        print("Ошибка ввода: вводите числа.")
        return

    # Вывод шапки таблицы
    print("-" * 35)
    print(f"| {'X':^12} | {'Y':^18} |")
    print("-" * 35)

    x = x_start
    while x <= x_end + 1e-9:
        y = calculate_y(x)
        print(f"| {x:12.4f} | {y:18.4f} |")
        x += dx

    print("-" * 35)


# ВОТ ЭТА СТРОКА ЗАПУСКАЕТ ПРОГРАММУ. ЕСЛИ ЕЕ НЕТ, КОНСОЛЬ БУДЕТ ПУСТОЙ.
if __name__ == "__main__":
    main()