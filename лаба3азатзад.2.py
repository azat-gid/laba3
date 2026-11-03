import random


def main():
    print("--- Лабораторная работа №3. Задание 2 (Мишень №3) ---")

    while True:
        try:
            R = float(input("Введите радиус мишени R (например, 10): "))
            if R > 0:
                break
            else:
                print("Радиус должен быть больше нуля!")
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")

    shots_count = 10
    print(f"\n--- Начинаем {shots_count} выстрелов по мишени с радиусом R = {R} ---")

    for i in range(1, shots_count + 1):
        # Генерируем координаты от -R до R
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        is_hit = False

        # --- ПРОВЕРКА УСЛОВИЙ ПОПАДАНИЯ ---

        # Проверяем, что точка внутри круга радиуса R
        inside_circle = (x ** 2 + y ** 2) <= R ** 2

        # 1. Левая верхняя четверть (X <= 0, Y >= 0)
        if x <= 0 and y >= 0 and inside_circle:
            is_hit = True

        # 2. Правая нижняя четверть (X >= 0, Y <= 0)
        elif x >= 0 and y <= 0 and inside_circle:
            is_hit = True

        # --- ВЫВОД РЕЗУЛЬТАТА ---
        x_round = round(x, 2)
        y_round = round(y, 2)

        if is_hit:
            print(f"Выстрел {i:2}: (X={x_round:6}, Y={y_round:6}) -> ПОПАДАНИЕ!")
        else:
            print(f"Выстрел {i:2}: (X={x_round:6}, Y={y_round:6}) -> промах.")

    print("\n--- Стрельба завершена ---")


if __name__ == "__main__":
    main()