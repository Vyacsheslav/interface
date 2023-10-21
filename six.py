Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> def clicked():
	 res = "Привет {}".format(txt.get())
	 lbl.configure(text=res)

	 
>>> window = Tk()
>>> window.title("Добро пожаловать в приложение PythonRu")
''
>>> window.geometry('400x250')
''
>>> lbl = Label(window, text="Привет")
>>> lbl.grid(column=0, row=0)
>>> txt = Entry(window,width=10)
>>> txt.grid(column=1, row=0)
>>> btn = Button(window, text="Клик!", command=clicked)
>>> btn.grid(column=2, row=0)
>>> window.mainloop()
>>> 
