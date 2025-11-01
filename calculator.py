"""
Простой калькулятор: выполняет базовые арифметические операции над двумя числами.
"""


def get_number(prompt):
    """Получает число от пользователя с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")


def calculate(num1, num2):
    """Выполняет арифметические операции и возвращает результаты."""
    results = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Ошибка: деление на ноль!"
    }
    return results


def main():
    print("Простой калькулятор (поддерживает +, -, *, /)")

    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")

    results = calculate(num1, num2)

    print("\nРезультаты:")
    for operation, result in results.items():
        print(f"Результат для {operation}: {result}")


if __name__ == "__main__":
    main()
