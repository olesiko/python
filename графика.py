from tkinter import *

root = Tk("моя программа")
frame = Frame(root,padx=10,pady=10,)
frame.grid()
# Label(frame, text="привет мир").grid(column=0,row=0)
# Label(frame, text="я ем шоколадку").grid(column=1,row=1)
# button = Button(frame, text="текст для кнопки",width=10,height=10)
# button.grid(column=2,row=2)
# button.grid(column=0,row=2)
Label(frame, text="текс").grid(column=0,row=0)
Button(frame, text="кнопка",background="#ba3232",width=10,height=10).grid(column=1,row=0)
Label(frame, text="текс").grid(column=2,row=0)
Button(frame, text="кнопка",background="#af13e8",width=10,height=10).grid(column=0,row=1)
Button(frame, text="кнопка",background="#13dae8",width=10,height=10).grid(column=1,row=1)
Button(frame, text="кнопка",background="#13e836",width=10,height=10).grid(column=2,row=1)
Label(frame, text="текс").grid(column=0,row=2)
Button(frame, text="кнопка",background="#e4e813",width=10,height=10).grid(column=1,row=2)
Label(frame, text="текс").grid(column=2,row=2)
root.mainloop()










