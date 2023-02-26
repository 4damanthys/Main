class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe ... ")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco", False)
    print(c.nome)

criar_cachorro()