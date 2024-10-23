import tkinter as tk

window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(0, 0)

button_add = tk.Button(window, text="+", width=2, height=2)
button_sub = tk.Button(window, text="-", width=2, height=2)
button_mul = tk.Button(window, text="*", width=2, height=2)
button_div = tk.Button(window, text="/", width=2, height=2)

number1_entry = tk.Entry(window, width=28)
number2_entry = tk.Entry(window, width=28)
answer_entry = tk.Entry(window)

number1 = tk.Label(window, text="Введите первое число")
number2 = tk.Label(window, text="Введите второе число")
answer = tk.Label(window, text="Ответ: ")

number1.place(x=100, y=50)
number2.place(x=100, y=125)
answer.place(x=100, y=275)
number1_entry.place(x=100, y=75)
number2_entry.place(x=100, y=150)
answer_entry.place(x=100, y=300)
button_add.place(x=100, y=200)
button_sub.place(x=150, y=200)
button_mul.place(x=200, y=200)
button_div.place(x=200, y=200)
window.mainloop()