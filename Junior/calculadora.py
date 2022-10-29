from tkinter import *
from tkinter import ttk
def funcion(x: int, y: int) -> list:
    """
        Toma dos numeros enteros y los convierte en una lista de dos elementos.
    Parametros:
        x (int) primer numero entero.
        y (int) segundo numero entero.
    Retorna:
        list: lista de dos elementos creada a partir de los numeros ingresados.
    """
    return [x,y]

root = Tk()
mainframe = ttk.Frame(root, padding=10)
mainframe.grid()
ttk.Label(mainframe, text="Hello world!").grid(column=0, row=0)
ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=2, row=2)
root.mainloop()