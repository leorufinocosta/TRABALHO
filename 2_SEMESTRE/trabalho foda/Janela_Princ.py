from tkinter import *
from tkinter import messagebox
from Janela_Uno import Uno
from Janela_Mobi import Mobi
from Janela_Argo import Argo
from Janela_Golf import Golf
from Janela_Toro import Toro

class Janela_Princ(Tk):
    def __init__(self, controle):
        #atributos
        self.controle = controle
        super().__init__()
        self.geometry('300x300+200+200')
        self.title('Concessionária')
        self.config(bg='black')

        #Widgets na tela
        self.bt1 = Button(self, width=18, text='UNO ATTRACTIVE\n '
                                               '1.0 FLEX MANUAL\n', bg='white', command=self.carro_uno)
        self.bt1.pack(padx= 0, pady=10)
        self.bt2 = Button(self, width=18, text='MOBI EASY\n '
                                               '1.0 FLEX MANUAL\n', bg='white', command=self.carro_mobi)
        self.bt2.pack(padx=0, pady=10)
        self.bt3 = Button(self, width=18, text='ARGO PRECISION\n '
                                               '1.8 AUTOMÁTICO FLEX\n', bg='white', command=self.carro_argo)
        self.bt3.pack(padx=0, pady=10)
        self.bt4 = Button(self, width=18, text='GOLF COMFORTLINE\n '
                                               '2.0 AUTOMÁTICO\n', bg='white', command=self.carro_golf)
        self.bt4.pack(padx=0, pady=10)
        self.bt5 = Button(self, width=18, text='TORO FREEDOM\n '
                                               '1.8 FLEX AUTOMÁTICO\n', bg='white', command=self.carro_toro)
        self.bt5.pack(padx=0, pady=10)

        self.menu = Menu(self)
        #Criando um item de menu e subitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Compradores')
        self.menu_principal.add_command(label='Vendas')
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair', command=self.fechar)
        self.menu.add_cascade(label='Consultar', menu=self.menu_principal)

        #Mostrando o mnenu
        self.config(menu=self.menu)

    def fechar(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()

    def carro_uno(self):
        Uno(self)

    def carro_mobi(self):
        Mobi(self)

    def carro_argo(self):
        Argo(self)

    def carro_golf(self):
        Golf(self)

    def carro_toro(self):
        Toro(self)