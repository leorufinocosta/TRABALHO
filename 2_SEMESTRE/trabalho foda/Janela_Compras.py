from tkinter import *
from tkinter import messagebox
from Nota_Fiscal_Uno import Nota

class Compras(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('270x270+200+200')
        self.title('REALIZANDO COMPRA')
        self.transient(parent)
        self.grab_set()
        self.text1 = Label(self, text="Dados do Comprador")
        self.text1.pack()
        self.text2 = Label(self, text="Nome")
        self.text2.place(x=10, y=30)
        self.text3 = Label(self, text="CPF")
        self.text3.place(x=10, y=50)
        self.text4 = Label(self, text="CEP")
        self.text4.place(x=10, y=70)
        self.entra1 = Entry(self)
        self.entra1.place(x=60, y=30)
        self.entra2 = Entry(self)
        self.entra2.place(x=60, y=50)
        self.entra3 = Entry(self)
        self.entra3.place(x=60, y=70)
        self.text5 = Label(self, text="Dados da Venda")
        self.text5.place(x=90, y=100)
        self.text6 = Label(self, text="Data da Venda")
        self.text6.place(x=10, y=130)
        self.text7 = Label(self, text="Valor da Venda")
        self.text7.place(x=10, y=150)
        self.entra4 = Entry(self)
        self.entra4.place(x=100, y=130)
        self.entra5 = Entry(self)
        self.entra5.place(x=100, y=150)
        self.bt1 = Button(self, width=15, text="Efetuar Compra", command=self.nota_fiscal)
        self.bt1.place(x=90, y=190)

    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()

    def nota_fiscal(self):
        Nota(self)


