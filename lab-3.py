import random
import winsound
import string
import threading
import tkinter as tk
from tkinter import messagebox

#музыка
def play_8bit_melody():
    notes = [
        (250, 300), (300, 300), (350, 300), (400, 600),
        (450, 300), (500, 600), (450, 300), (350, 300),
        (300, 300), (250, 300), (200, 600)
    ]
    while True:
        for freq, duration in notes:
            winsound.Beep(freq, duration)

music_thread = threading.Thread(target=play_8bit_melody, daemon=True)
music_thread.start()

#ключ
def make_key():
    num = entry_input.get().strip()

    if len(num) != 6 or not num.isdigit():
        messagebox.showerror("Ошибка", "Нужно ввести ровно 6 цифр!")
        return

    part1 = list(num[0:3])
    part2 = list(num[3:6])

    random.shuffle(part1)
    random.shuffle(part2)

    digits1 = "".join(part1)
    digits2 = "".join(part2)

    letters = string.ascii_uppercase
    b1_letters = random.choice(letters) + random.choice(letters)
    b2_letters = random.choice(letters) + random.choice(letters)

    block1 = digits2 + b1_letters
    block2 = digits1 + b2_letters

    sum_result = int(digits2) + int(digits1)
    block3 = str(sum_result).zfill(4)

    final_key = block1 + "-" + block2 + "-" + block3

    entry_result.delete(0, tk.END)
    entry_result.insert(0, final_key)

#анимация
def animate():
    colors = ["#00ff00", "#ff00ff", "#00ffff", "#ffff00"]
    current_color = label_title.cget("fg")

    if current_color == colors[0]:
        label_title.config(fg=colors[1])
    elif current_color == colors[1]:
        label_title.config(fg=colors[2])
    elif current_color == colors[2]:
        label_title.config(fg=colors[3])
    else:
        label_title.config(fg=colors[0])

    root.after(400, animate)


#окно
root = tk.Tk()
root.title("My Keygen")
root.geometry("800x500")

bg_img = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(relwidth=1, relheight=1)

label_title = tk.Label(root, text=" HSR KEYGEN ", font=("Arial", 16, "bold"), bg="black")
label_title.pack(pady=100)

label_input = tk.Label(root, text="Введи 6 цифр:", font=("Arial", 10), fg="white", bg="black")
label_input.pack(pady=5)

entry_input = tk.Entry(root, font=("Arial", 12), justify="center")
entry_input.pack(pady=5)

btn_generate = tk.Button(root, text="Сгенерировать ключ", command=make_key, bg="purple", fg="white",
                         font=("Arial", 11, "bold"))
btn_generate.pack(pady=10)

label_result = tk.Label(root, text="Твой ключ:", font=("Arial", 10), fg="white", bg="black")
label_result.pack(pady=5)

entry_result = tk.Entry(root, font=("Arial", 12), justify="center", width=25)
entry_result.pack(pady=5)

animate()
root.mainloop()
