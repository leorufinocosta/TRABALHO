from tkinter import *
from tkinter import messagebox
from Nota_Fiscal_Argo import Nota_Argo

class Argo(Toplevel):
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('DETALHES DA VENDA')
        self.transient(parent)
        self.grab_set()
        self.text = Label(self, text="COR VEICULO: PRETO")
        self.text.pack()
        self.text = Label(self, text="PORTAS: 4")
        self.text.pack()
        self.text = Label(self, text="ANO: 2019")
        self.text.pack()
        self.text = Label(self, text="FABRICANTE: FIAT")
        self.text.pack()
        self.text = Label(self, text="MODELO: ARGO PRECISION")
        self.text.pack()
        self.text = Label(self, text="PLACA: JFE-1002")
        self.text.pack()
        self.text = Label(self, text="PREÇO: R$50.640,00")
        self.text.pack()
        self.bt_venda = Button(self, width=10, text='COMPRAR', command=self.compras)
        self.bt_venda.pack(pady=10)
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()

    def compras(self):
        Nota_Argo(self)