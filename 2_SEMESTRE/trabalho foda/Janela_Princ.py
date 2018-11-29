from tkinter import *
from tkinter import messagebox
from Janela_Uno import Uno
from Janela_Mobi import Mobi
from Janela_Argo import Argo
from Janela_Cronos import Cronos
from Janela_Toro import Toro

class Janela_Princ(Tk):
    def __init__(self, controle):
        #atributos
        self.controle = controle
        super().__init__()
        self.geometry('300x300+200+200')
        self.title('Concessionária')

        #Widgets na tela
        self.bt1 = Button(self, width=10, text='Uno', command=self.carro_uno)
        self.bt1.pack(padx= 0, pady=10)
        self.bt2 = Button(self, width=10, text='Mobi', command=self.carro_mobi)
        self.bt2.pack(padx=0, pady=10)
        self.bt3 = Button(self, width=10, text='Argo', command=self.carro_argo)
        self.bt3.pack(padx=0, pady=10)
        self.bt4 = Button(self, width=10, text='Cronos', command=self.carro_cronos)
        self.bt4.pack(padx=0, pady=10)
        self.bt5 = Button(self, width=10, text='Toro', command=self.carro_toro)
        self.bt5.pack(padx=0, pady=10)

        self.menu = Menu(self)
        #Criando um item de menu e subitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Carros Disponíveis')
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

    def carro_cronos(self):
        Cronos(self)

    def carro_toro(self):
        Toro(self)