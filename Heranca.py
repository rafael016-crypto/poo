class Animal:
    def __init__(self, nome):
        self._nome = nome  # atributo protegido

    @property
    def nome(self):
        return self._nome

    def comer(self):
        print(f"{self.nome} está comendo")

    def dormir(self):
        print(f"{self.nome} está dormindo")


class Cachorro(Animal):  # Cachorro herda de Animal
    def latir(self):
        print(f"{self.nome} faz: Au au!")

    def comer(self):  # Sobrescrevendo método da classe pai
        print(f"{self.nome} está devorando a ração")


# Uso
rex = Cachorro("Rex")
rex.comer()    # Método sobrescrito
rex.latir()    #Método peóprio
rex.dormir()   # Método herdado
