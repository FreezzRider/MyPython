import tkinter as tk

# Создаём главное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)

# Строка для отображения выражения
expression = ""

# Функция обновления выражения
def press(symbol):
    global expression
    expression += str(symbol)
    entry_var.set(expression)

# Функция вычисления выражения
def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Ошибка")
        expression = ""

# Функция очистки
def clear():
    global expression
    expression = ""
    entry_var.set("")

# Переменная для строки ввода
entry_var = tk.StringVar()

# Поле ввода (только для отображения)
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify="right", bd=10, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки калькулятора
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0),
]

# Создание кнопок на окне
for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
              command=action).grid(row=row, column=col, padx=5, pady=5)

# Запуск главного цикла
root.mainloop()
