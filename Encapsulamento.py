class Pessoal:
    def __init__(self, nome):
        self._nome = nome  #atributo protegido

    def falar(self):
        print(f"Olá, meu nome é {self.nome}")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) > 0:
            self._nome = novo_nome
        else:
            raise ValueError("Nome não pode ser vazio")


p = Pessoal("Rafael")
p.falar()

print(p.nome) #acessando pelo getter
p.nome = "Ana" #alterando pelo setter
p.falar()

