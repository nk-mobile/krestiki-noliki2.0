# main.py (ветка logic)

import tkinter as tk
from tkinter import messagebox

# Создание окна приложения
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x380")

# Переменная для хранения текущего игрока
current_player = "X"

# Список для хранения всех кнопок игрового поля
buttons = []


# Функция для обработки кликов по кнопкам
def on_click(row, col):
    global current_player

    # Если кнопка уже занята, ничего не делаем
    if buttons[row][col]['text'] != "":
        return

    # Устанавливаем символ текущего игрока на кнопку
    buttons[row][col]['text'] = current_player

    # Проверяем, есть ли победитель
    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        disable_buttons()
        return

    # Проверяем на ничью
    if check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        disable_buttons()
        return

    # Меняем текущего игрока
    current_player = "O" if current_player == "X" else "X"


# Функция для проверки победителя
def check_winner():
    # Проверка горизонталей
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True

    # Проверка вертикалей
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Проверка главной диагонали
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    # Проверка побочной диагонали
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


# Функция для проверки ничьей
def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                return False
    return True


# Функция для отключения всех кнопок
def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")


# Функция для сброса игры
def reset_game():
    global current_player
    current_player = "X"

    # Очищаем все кнопки и включаем их
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")


# Создание игрового поля 3x3
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            window,
            text="",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j, padx=2, pady=2)
        row.append(btn)
    buttons.append(row)

# Создание кнопки сброса
reset_button = tk.Button(
    window,
    text="Новая игра",
    font=("Arial", 14),
    command=reset_game
)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Запуск главного цикла окна
window.mainloop()