import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def janela_principal():
    root = tk.Tk()
    root.title("The Math Game")
    root.geometry("800x600")
    root.resizable(False, False)
    root.continua_jogo= tk.BooleanVar(value=False)
    root.running = True
    
    
    def confirmacao():
        if messagebox.askyesno("confirmação","Voce tem certeza que quer sair?"):
            root.continua_jogo.set(True)
            root.continua_jogo = False
            root.destroy()
            
    root.protocol("WM_DELETE_WINDOW",confirmacao)
           
    root.mainloop()
janela_principal()