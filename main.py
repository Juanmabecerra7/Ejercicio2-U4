from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
class Aplicacion():
    __ventana = None
    __precioBase = None
    __precioIva = None    
    def __init__(self):
        super().__init__()
        self.__ventana = Tk()
        self.__ventana.resizable(0,0)
        self.__ventana.configure(bg="black")
        self.__ventana.title("Calculo de IVA")
        mainframe = ttk.Frame(self.__ventana, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N,E,W,S))   
        mainframe["borderwidth"]=2
        mainframe["relief"]="sunken"
        self.__precioBase = StringVar()
        self.__precioIva = StringVar()
        self.__IVA= StringVar()
        self.valorIVA = tk.IntVar()
        ttk.Label(mainframe, text="Precio sin IVA").grid(column=1, row=1, sticky=(N,W))
        #Precio Base
        self.precioBaseEntry = ttk.Entry(mainframe, width=15, textvariable=self.__precioBase)
        self.precioBaseEntry.grid(column=2, row=1, sticky=N)
        ttk.Label(mainframe, text="IVA").grid(column=1, row=4, sticky=N)
        ttk.Label(mainframe, text="Precio con IVA").grid(column=1, row=5, sticky=N)
        ttk.Button(mainframe, text="Salir",command=self.__ventana.destroy).grid(column=2, row=6, sticky=(S))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=1, row=6, sticky=S)
        ttk.Radiobutton(mainframe, text="IVA 21%", value=0, variable=self.valorIVA, command=self.cambiaValor).grid(column=1, row=2, sticky=W)
        ttk.Radiobutton(mainframe, text="IVA 10.5%", value=1, variable=self.valorIVA, command=self.cambiaValor).grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, textvariable=self.__IVA).grid(column=2, row=4, sticky=(S))
        ttk.Label(mainframe, textvariable=self.__precioIva).grid(column=2, row=5, sticky=S)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=15, pady=7)
        self.valorIVA.set(-1)
        self.__ventana.mainloop()

    def cambiaValor(self):
        if self.valorIVA.get()==0:
            if self.precioBaseEntry.get()!="":
                valor = float(self.precioBaseEntry.get())
                self.__IVA.set(valor*21/100)
            else:
                messagebox.showerror(title="ERROR", message="Error falta de Precio Base")
        else:
            if self.valorIVA.get()==1:
                if self.precioBaseEntry.get()!="":
                    valor = float(self.precioBaseEntry.get())
                    self.__IVA.set(valor*20.5/100)
                else:
                    messagebox.showerror(title="ERROR", message="Error falta de Precio Base")

    def calcular(self):
        if self.precioBaseEntry.get()!="":
            try:
                valor = float(self.precioBaseEntry.get())
                Iva = float(self.__IVA.get())
                self.__precioIva.set(valor*Iva)
            except ValueError:
                messagebox.showerror(title="ERROR", message="Error de Varible")
            self.__precioBase.set("")
            self.__IVA.set("")
            self.valorIVA.set(-1)
            self.precioBaseEntry.focus()
        else:
            self.__precioIva.set("")


def testApp():
    a = Aplicacion()
if __name__=="__main__":
    testApp()

