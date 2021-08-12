class funcionario(object):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumenta_cinco_porcento(self):
        self.salario = self.salario + (self.salario * 0.05)
    
    def aumenta_dez_porcento(self):
        self.salario = self.salario + (self.salario * 0.1)
        print(f"O sorteado foi: {self.nome}, agora tendo um salário de: {self.salario}")