from tkinter import *
from tkinter import ttk

# /---- Bindings ----/ # Interações com a tela

root = Tk()

l = ttk.Label(root, text='Começando...')
l.grid()
l.bind('<Enter>', lambda e: l.configure(text="Movido o mouse para dentro"))
l.bind('<Leave>', lambda e: l.configure(text="Movido o mouse para fora"))
l.bind('<1>', lambda e: l.configure(text="Clicou o botão esquerdo do mouse"))
l.bind('<Double-1>', lambda e: l.configure(text="Duplo click"))
l.bind('<B3-Motion>', lambda e: l.configure(text="Arraste o botão direito para %d, %d" % (e.x, e.y)))


root.mainloop()