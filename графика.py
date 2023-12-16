from tkinter import *
# создаем окошко программф

def AnyKey():
    print("кнопка жмакнута")
    label.configure(text="текст поменялся")

root = Tk("моя программа")
# работаем с окошком
root.geometry("500x300")
# можно ли изменять размер окна
root.resizable(width=True,height=True)
# цвет окошка
root["bg"] = "black"

frame = Frame(root,padx=100,pady=10,width=200,height=200)
# настраиваем местоположение фрейма
frame.place(anchor="e", relx=1, rely=0.5)
Button(frame,text="кнопка",fg="white",bg="green",width=10,height=10,wraplength=100,command=AnyKey).grid(column=0,row=1)
label = Label(frame,text="заголовок")
label.grid(column=0,row=0)


frame2 = Frame(root,padx=100,pady=10,width=200,height=200)
frame2.place(anchor="w", relx=0, rely=0.5)
frame2["bg"] = "red"




# Label(frame, text="привет мир").grid(column=0,row=0)
# Label(frame, text="я ем шоколадку").grid(column=1,row=1)
# button = Button(frame, text="текст для кнопки",width=10,height=10)
# button.grid(column=2,row=2)
# button.grid(column=0,row=2)
# Label(frame, text="текс").grid(column=0,row=0)
# Button(frame, text="кнопка",background="#ba3232",width=10,height=10).grid(column=1,row=0)
# Label(frame, text="текс").grid(column=2,row=0)
# Button(frame, text="кнопка",background="#af13e8",width=10,height=10).grid(column=0,row=1)
# Button(frame, text="кнопка",background="#13dae8",width=10,height=10).grid(column=1,row=1)
# Button(frame, text="кнопка",background="#13e836",width=10,height=10).grid(column=2,row=1)
# Label(frame, text="текс").grid(column=0,row=2)
# Button(frame, text="кнопка",background="#e4e813",width=10,height=10).grid(column=1,row=2)
# Label(frame, text="текс").grid(column=2,row=2)
root.mainloop()










