import tkinter as tk

def on_button_click(event):
    # Получаем текст с кнопки, на которую нажали
    button_text = event.widget.cget("text")
    
    # Обработка нажатия кнопки "="
    if button_text == "=":
        try:
            result = eval(entry.get())  # Вычисляем выражение
            entry.delete(0, tk.END)  # Очищаем поле ввода
            entry.insert(tk.END, str(result))  # Выводим результат
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")

    # Обработка нажатия кнопки "C" (сброс)
    elif button_text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, button_text)

# Создаем главное окно приложения
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Создаем кнопки
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
column = 0

for button_label in buttons:
    button = tk.Button(root, text=button_label, width=5)
    button.grid(row=row, column=column)
    button.bind("<Button-1>", on_button_click)
    column += 1
    
    # Разделение кнопок на ряды
    if column > 3:
        column = 0
        row += 1

# Запускаем главный цикл приложения
root.mainloop()
