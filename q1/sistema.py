import Classe
from random import randrange

funcionarios = []
qtd_atual = 0;

while(len(funcionarios) < 10):
    atual = len(funcionarios)+1
    nome = input(f"Insira o nome do {atual}° funcionário: ")
    salario = int(input(f"Insira o salário do {atual}° funcionário: "))
    funcionarios.append(Classe.funcionario(nome, salario))
    qtd_atual += 1
    if(qtd_atual == 3):
        for i in range(len(funcionarios)):
            funcionarios[i].aumenta_cinco_porcento()
            qtd_atual = 0
    
sorteado = randrange(10)
funcionarios[sorteado].aumenta_dez_porcento()