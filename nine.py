from tkinter import *
from tkinter.ttk import Checkbutton
window = Tk()
window.title("Добро пожаловать в приложение PythoneRu")
window.geometry('400x250')
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column= 0, row= 0)
window.mainloop()