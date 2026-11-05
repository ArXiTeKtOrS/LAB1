import sys

class PowerPair:
    def __init__(self, first, second):
        """
        Инициализация полей с проверкой корректности типов и значений.
        first — дробное (или целое) число.
        second — целое число (показатель степени).
        """
        if not isinstance(first, (int, float)):
            raise ValueError("Ошибка: Поле 'first' должно быть числом (дробным или целым).")
        if not isinstance(second, int):
            raise ValueError("Ошибка: Поле 'second' должно быть целым числом.")
        if first == 0 and second < 0:
            raise ValueError("Ошибка: Возведение нуля в отрицательную степень невозможно.")
            
        self.first = float(first)
        self.second = second

    def read(self):
        """Ввод значений полей с клавиатуры с проверкой на корректность."""
        while True:
            try:
                f = float(input("Введите дробное число (first): "))
                s = int(input("Введите целое число (second, показатель степени): "))
                # Проверяем на деление на ноль при отрицательной степени
                if f == 0 and s < 0:
                    print("Ошибка: Ноль нельзя возводить в отрицательную степень. Попробуйте снова.")
                    continue
                self.first = f
                self.second = s
                break
            except ValueError:
                print("Некорректный ввод! Пожалуйста, введите корректные числа.")

    def display(self):
        """Вывод значений полей на экран."""
        print(f"Поля класса: first = {self.first}, second = {self.second}")

    def power(self):
        """Возведение числа first в степень second."""
        try:
            return self.first ** self.second
        except OverflowError:
            print("Ошибка: Результат вычислений слишком велик (переполнение).")
            return None


def make_power_pair(first, second):
    """
    Внешняя функция для создания объекта.
    При передаче ошибочных параметров выводит сообщение и завершает работу.
    """
    try:
        return PowerPair(first, second)
    except ValueError as e:
        print(f"[Критическая ошибка make_power_pair]: {e}")
        sys.exit(1)
