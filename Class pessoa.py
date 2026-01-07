class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Olá, meu nome é", self.nome)
        print("Minha idade é ", self.idade, "anos")

# criando um objeto corretamente
p1 = Pessoa("Rafael Freitas da Silva", 27)

# chamando o método
p1.falar()


#self significa o próprio objeto


class carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        #self significa o próprio objeto

    def falar(self):
        print("A marca do meu carro é um", self.marca)
        print("A cor do meu carro é ", self.cor)

# criando um objeto corretamente
p1 = carro ("Bugatti", "vermelho")

# chamando o método
p1.falar()
