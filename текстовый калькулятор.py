def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

while True:
    print("\nПростой калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")

    choice = input("Выберите операцию (1/2/3/4/5): ")

    if choice == "5":
        print("Выход из программы. До свидания!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Ошибка: неправильный выбор. Попробуйте снова.")
        continue

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите корректные числа.")
        continue

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)

    print("Результат:", result)
