from tkinter import *
from tkinter import messagebox
from Janela_Compras import Compras

class Nota(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('270x270+200+200')
        self.title('NOTA FISCAL')
        self.transient(parent)
        self.grab_set()
        self.lb1 = Label(self, text="Compra Efetuada").pack()
        self.lb2 = Label(self, text='Nome: '+self.Compras.entra1).pack()
        self.lb3 = Label(self, text="CPF: "+self.Compras.entra2).pack()


    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()