import tkinter as tk
from utilitarios import resetaTela, rodape
from tela_jogo import TelaJogo

class TelaInstrucoes:
    def __init__(self,root):
        self.root = root

    def frameTelaInstrucoes(self):
        resetaTela(self.root)
        self.root.title("The Masth Game")

        titulo = tk.Label(self.root, text="Instruções", font=("Arial",24))
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root, 
            text="Clique na operação que corresponde ao resultados entre os dois números")

        texto.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Jogar",
            command=self.abrirTelajogo,
            font=("Arial",16),
            width=10,
            height=2
        )
        
        botao_play.pack(pady=20)

        rodape(self.root)
        

    def abrirTelajogo(self):
        tela_jogo = TelaJogo(self.root)
        tela_jogo.frameTelaJogo()