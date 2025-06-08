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

print("Простой калькулятор на Python")
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if choice == "1":
    result = add(a, b)
elif choice == "2":
    result = subtract(a, b)
elif choice == "3":
    result = multiply(a, b)
elif choice == "4":
    result = divide(a, b)
else:
    result = "Ошибка: неверный выбор операции"

print("Результат:", result)
