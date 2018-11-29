from tkinter import *
from tkinter import messagebox

class Argo(Toplevel):
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('ARGO')
        self.transient(parent)
        self.grab_set()

    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja Sair?'):
            super().destroy()