import tkinter as tk
def destruir(root):
    for widget in root.winfo_children():
        widget.destroy()