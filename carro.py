class Carro:
    def __init__(self):
        self.__ligado = False  # Detalhes de implementação internos (não visíveis ao usuário)
        self.__velocidade = 0

    def ligar_desligar(self):  # Método público que lida com a lógica interna
        if self.__ligado:
            self.__ligado = False
            self.__velocidade = 0
            print("Carro desligado.")
        else:
            self.__ligado = True
            print("Carro ligado.")

    def acelerar(self, valor):  # Método público para acelerar
        if self.__ligado:
            self.__velocidade += valor
            print(f"Acelerando... Velocidade atual: {self.__velocidade} km/h")
        else:
            print("O carro está desligado. Ligue-o primeiro.")

# --- Uso da abstração ---
meu_carro = Carro()

# O usuário interage apenas com os métodos públicos
meu_carro.ligar_desligar()
meu_carro.acelerar(50)
meu_carro.ligar_desligar()
meu_carro.acelerar(20)  # Não vai funcionar, pois o carro está desligado
