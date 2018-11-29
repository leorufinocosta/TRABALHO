from tkinter import *
from tkinter import messagebox
from Nota_Fiscal_Toro import Nota_Toro

class Toro(Toplevel):
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('DETALHES DA VENDA')
        self.transient(parent)
        self.grab_set()
        self.text = Label(self, text="COR VEICULO: VERMELHO")
        self.text.pack()
        self.text = Label(self, text="PORTAS: 4")
        self.text.pack()
        self.text = Label(self, text="ANO: 2019")
        self.text.pack()
        self.text = Label(self, text="FABRICANTE: FIAT")
        self.text.pack()
        self.text = Label(self, text="MODELO: TORO FREEDOM")
        self.text.pack()
        self.text = Label(self, text="PLACA: JAS-1201")
        self.text.pack()
        self.text = Label(self, text="PREÇO: R$104.990")
        self.text.pack()
        self.bt_venda = Button(self, width=10, text='COMPRAR', command=self.compras)
        self.bt_venda.pack(pady=10)
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()

    def compras(self):
        Nota_Toro(self)