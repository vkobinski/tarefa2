import math

def converte_real_dolar(reais):
    dolar = 5.30
    if(reais % dolar == 0):
        print(f" Podem ser comprados: {reais/dolar} dólares")
        return
    print(f"Podem ser comprados: {math.floor(reais/dolar)} dólares")