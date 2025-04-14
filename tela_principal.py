import tkinter as tk
from tkinter import messagebox
from tela_abertura import TelaInicial
from tela_instrucoes import TelaInstrucoes

def janela_principal():
    root=tk.Tk()
    root.title("The Math Game ")
    root.geometry("800x600")
    root.resizable(False,False)

    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True

    def fechar_janela():

        if messagebox.askyesno("Confirmação","Você quer sair ?"):
            root.runnig = False
            root.continua_jogo.set(True)
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", fechar_janela)
    return root
    
if __name__ == "__main__":
    root = janela_principal()
    tela_inicial = TelaInicial(root)
    tela_inicial.constroiLayout()
    
    root.mainloop()
