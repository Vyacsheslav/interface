Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> window = Tk()
>>> window.title("Добро пожаловать в приложение PythonRu")
''
>>> window.geometry('400x250')
''
>>> lbl = Label(window, text="Привет", font=("Arial Bold", 50))
>>> lbl.grid(column=0, row=0)
>>> btn = Button(window, text="Не нажимать!")
>>> btn.grid(column=1, row=0)
>>> window.mainloop()
