# 26/02/2023
# Primeiro Programa em POO (Programação Orientada a Objetos)

# NOSSO PRIMEIRO PROGRAMA POO:
# João tem uma biciletaria e gostaria de registrar as vendas de  suas bicicletas. Crie um programa onde João informe: cos, modelo, ano e valor da 
# bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

class Bicileta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Blim ...")
    
    def parar(self):
        print("Bicicleta parada.")
    
    def correr(self):
        print("Vrum")
    
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join({f'{chave}={valor}' for chave, valor in self.__dict__.items()})}"

b1 = Bicileta("vermelha", "caloi", 2022, 600)
b1.parar()
b1.buzinar()
b1.correr()
b2 = Bicileta("verde", "monark", 2000, 189)

Bicileta.buzinar(b1)
print(b2)