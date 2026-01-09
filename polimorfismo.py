class Terrestre:
    def andar(self):
        print("Andando na terra")

class Aquatico:
    def nadar(self):
        print("Nadando na água")

class Anfibio(Terrestre, Aquatico):
    pass

sapo = Anfibio()

sapo.andar()  # Método da classe Terrestre
sapo.nadar()  # Método da classe Aquatico
