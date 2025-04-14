import tkinter as tk
import time  # Adicionado para medir o tempo da resposta
from utilitarios import resetaTela, rodape
from logica_jogo import dadosFuncionais

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.num1 = 0
        self.num2 = 0
        self.operador = ""
        self.resultado = 0

        self.pontuacao_valor = 0
        self.pontuacao = tk.StringVar(value="0")

        self.tempo_valor = 0
        self.tempo = tk.StringVar(value="0")

        self.partida_valor = 0
        self.partida = tk.StringVar(value="0")

        self.rodando = True
        self.tempo_inicio_questao = 0  # Armazena quando a questão começou

    def gerarQuestao(self):
        self.num1, self.num2 = dadosFuncionais.gerarNumeros()
        self.operador = dadosFuncionais.selecionarOperador()
        self.resultado = dadosFuncionais.calcularResultado(self.num1, self.num2, self.operador)

    def frameTelaJogo(self):
        resetaTela(self.root)
        self.root.title("The Math Game")
        self.gerarQuestao()

        cabecalho = tk.Frame(self.root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Pontuação: ").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, textvariable=self.pontuacao).grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Partida: ").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, textvariable=self.partida).grid(row=0, column=3, padx=10)

        tk.Label(cabecalho, text="Tempo: ").grid(row=0, column=4, padx=10)
        tk.Label(cabecalho, textvariable=self.tempo).grid(row=0, column=5, padx=10)

        botao_parar = tk.Button(cabecalho, text="Parar", font=("Arial", 10), command=lambda: self.pararJogo(self.root))
        botao_parar.grid(row=0, column=6, padx=10)

        self.numeros_frame = tk.Frame(self.root)
        self.numeros_frame.pack(pady=40)

        self.label_num1 = tk.Label(self.numeros_frame, text=str(self.num1), font=("Arial", 32))
        self.label_num1.pack(side="left", padx=20)

        self.label_operador = tk.Label(self.numeros_frame, text="?", font=("Arial", 32))
        self.label_operador.pack(side="left", padx=20)

        self.label_num2 = tk.Label(self.numeros_frame, text=str(self.num2), font=("Arial", 32))
        self.label_num2.pack(side="left", padx=20)

        tk.Label(self.numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=20)

        self.label_resultado = tk.Label(self.numeros_frame, text=str(self.resultado), font=("Arial", 32))
        self.label_resultado.pack(side="left", padx=20)

        operacoes_frame = tk.Frame(self.root)
        operacoes_frame.pack(pady=30)

        for operacao in ["+", "-", "X", "÷"]:
            tk.Button(
                operacoes_frame,
                text=operacao,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda op=operacao: self.verificaResposta(op)
            ).pack(side="left", padx=10)

        self.mensagem = tk.Label(self.root, text="", font=("Arial", 16))
        self.mensagem.pack(pady=10)

        rodape(self.root)
        self.tempo_inicio_questao = time.time()
        self.atualizaTempo()

    def verificaResposta(self, resposta_usuario):
        operador_real = self.operador
        if operador_real == "*":
            operador_real = "X"
        elif operador_real == "/":
            operador_real = "÷"

        tempo_resposta = time.time() - self.tempo_inicio_questao

        if resposta_usuario == operador_real:
            mensagem_bonus = ""
            self.pontuacao_valor += 100

            if tempo_resposta < 5:
                self.pontuacao_valor += 500
                mensagem_bonus = " ⏱️ +500 por rapidez!"

            self.mensagem.config(text=f"✅ Correto!{mensagem_bonus}", fg="green")
            self.pontuacao.set(str(self.pontuacao_valor))
        else:
            self.mensagem.config(text=f"❌ Errado!", fg="red")

        self.root.after(1000, self.proximaQuestao)

    def proximaQuestao(self):
        if self.partida_valor < 100:
            self.partida_valor += 1
            self.partida.set(str(self.partida_valor))

        if self.partida_valor >= 100:
            self.mensagem.config(text="🏁 Fim de Jogo!", fg="blue")
            self.rodando = False
            return

        self.gerarQuestao()
        self.label_num1.config(text=str(self.num1))
        self.label_num2.config(text=str(self.num2))
        self.label_resultado.config(text=str(self.resultado))
        self.label_operador.config(text="?")
        self.mensagem.config(text="")
        self.tempo_inicio_questao = time.time()

    def atualizaTempo(self):
        if self.rodando:
            self.tempo_valor += 1
            self.tempo.set(str(self.tempo_valor))
            self.root.after(1000, self.atualizaTempo)

    def pararJogo(self, root):
        self.rodando = False
        root.running = False
        root.continua_jogo.set(True)
