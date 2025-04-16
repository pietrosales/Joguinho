# recorde.py

import os

ARQUIVO_RECORDE = "recorde.txt"

def carregar_recorde():
    if os.path.exists(ARQUIVO_RECORDE):
        with open(ARQUIVO_RECORDE, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0

def salvar_recorde(nova_pontuacao):
    atual = carregar_recorde()
    if nova_pontuacao > atual:
        with open(ARQUIVO_RECORDE, "w") as f:
            f.write(str(nova_pontuacao))
