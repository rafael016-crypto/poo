class contabancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial # O atributo "__saldo" é privado (encapsulado) por convenção.

        #Métado para depositar dinheiro

    def depositar(self, valor):
        if valor> 0:
            self._saldo += valor
            print(f" Depósito de R$ {valor:.2f} realizado.")

        else:
             print(f" O valor de depósito deve ser positivo.")

        # Método para sacar dinheiro 
    
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print (f" Saque de R$ {valor:.2f} realizado.")
            return True
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
            return False
        # Método para obter o saldo (getter)

    def get_saldo(self):
        return self._saldo
    # ===== USO DA CLASSE =====
minha_conta = contabancaria("Rafael", 150)

minha_conta.depositar(50)
print(f"Saldo atual: R$ {minha_conta.get_saldo():.2f}")

minha_conta.sacar(70)
print(f"Saldo atual: R$ {minha_conta.get_saldo():.2f}")

minha_conta.sacar(200)  # Essa ação não será permitida
print(f"Saldo atual: R$ {minha_conta.get_saldo():.2f}")
