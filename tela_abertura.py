import tkinter as tk
from tela_instrucoes import TelaInstrucoes
from utilitarios import resetaTela, rodape

class TelaInicial:
    def __init__(self,root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game")


    def constroiLayout(self):
        tk.Label(self.root,text="The Math Game",font=("Arial",30)).pack()
        
        button = tk.Button(self.root,text="Play",command=self.abrirInstrucoes,font=("Arial",12))
        button.pack(pady=10)

        rodape(self.root)
    

    def abrirInstrucoes(self):
        Tela_Instrucoes = TelaInstrucoes(self.root)
        Tela_Instrucoes.frameTelaInstrucoes()

