import tkinter
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл', filetypes=(('text files', '*.txt'), ('all files', '*.*')))
    text['text'] = text['text'] + filename

window = tkinter.Tk()
window.configure(bg='black')
window.title('Проводник')
window.geometry('350x350')
window.resizable(0, 0)
text = tkinter.Label(window, text='Файл: ', height=10, width=50, background='silver', foreground='blue')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', height=3, width=20, foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=5) 
window.mainloop()