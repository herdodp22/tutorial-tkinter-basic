from tkinter import*
from typing import Collection

root = Tk()

kotak1 = Label(root, text="nama")
kotak2 = Label(root, text="alamat")
kotak3 = Label(root, text="no. hp")

edit1 = Entry(root)
edit2 = Entry(root)
edit3 = Entry(root)

kotak1.grid(row=0)
kotak2.grid(row=1)
kotak3.grid(row=2)

edit1.grid(row=0, column=1)
edit2.grid(row=1, column=1)
edit3.grid(row=2, column=1)

root.mainloop()