import random

class boleto(object):
    def __init__(self, banco, mes, dia, ano, valor):
        aleatorio = random.randint(1000, 10000)
        print("Boleto gerado: ")
        print(f"{banco} | {aleatorio}{mes}{dia}{ano}00000000{valor}")

    def novo_boleto():
        banco = input("Insira o número do banco: ")
        mes = input("Insira o mês: ")
        dia = input("Insira o dia: ")
        ano = input("Insira o ano: ")
        valor = input("Insira o valor do boleto: ")
        boleto(banco, mes, dia, ano, valor)