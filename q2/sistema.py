import Classe
import os

continuar = True
while(continuar):
    Classe.boleto.novo_boleto()
    mudanca = input(f"Deseja continuar? s/n {os.linesep}")
    if(mudanca == "n"):
        continuar = False
    print("\n" * os.get_terminal_size().lines)