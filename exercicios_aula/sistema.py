import time
import os
import q11
import q12
import q13
import q14
import q15
import q16
import random

continuar = True
while(continuar):
    print("\n" * os.get_terminal_size().lines)
    print("1 - Converte real para dólar.")
    print("2 - Quantidade tinta.")
    print("3 - Desconto de 5%.")
    print("4 - Aumento de 15%.")
    print("5 - Conversão Celsius-Fahrenheit.")
    print("6 - Carro alugado.")
    print("7 - Limpar o quadro.")
    print("0 - Parar sistema.")
    escolha = int(input("Qual serviço deseja utilizar? "))

    if(escolha == 1):
        real = float(input("Insira o valor em reais: "))
        q11.converte_real_dolar(real)
        time.sleep(5)
    
    elif(escolha == 2):
        largura = int(input("Insira a largura da parede: "))
        altura = int(input("Insira a altura da parede:"))
        q12.pintar_parede(largura, altura)
        time.sleep(5)

    elif(escolha == 3):
        preco = float(input("Insira o preço do produto: "))
        q13.desconto_cinco_porcento(preco)
        time.sleep(5)

    elif(escolha == 4):
        salario = float(input("Insira o salário: "))
        q14.salario_aumento(salario)
        time.sleep(5)
    
    elif(escolha == 5):
        celsius = float(input("Insira a temperatura em celsius: "))
        q15.fahrenheit(celsius)
        time.sleep(5)

    elif(escolha == 6):
        km_rodados = int(input("Insira a quantidade de Km rodados: "))
        diarias = int(input("Insira a quantidade de dias que o carro foi alugado: "))
        q16.calculo(km_rodados, diarias)
        time.sleep(5)

    elif(escolha == 7):
        qtd_alunos = int(input("Insira a quantidade de alunos: "))
        alunos = []
        while(len(alunos) < qtd_alunos):
            alunos.append(input("Nome do aluno: "))
        sorteado = random.randint(0, qtd_alunos)
        print(f"Aluno sorteado: {alunos[sorteado]}")
        time.sleep(5)
    
    else:
        continuar = False