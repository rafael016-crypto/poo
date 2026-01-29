def tabuada (numero):
    operacoes = ["adição", "subtração", "multiplicação", "divisão"]

    op = 0
    #O while vai repetir enquanto op for menor que o tamanho da lista.
    while op < len(operacoes):
        print(f"\n{operacoes[op].upper()}")

        for i in range(1, 11):
            if operacoes[op] == "adição":
                print(f"{numero} + {i} = {numero + i}")

            elif operacoes[op] == "subtração":
                print(f"{numero} - {i} = {numero - i}")

            elif operacoes[op] == "multiplicação":
                print(f"{numero} x {i} = {numero * i}")

            elif operacoes[op] == "divisão":
                print(f"{numero} ÷ {i} = {numero / i:.2f}")

        op += 1

    print(f"\n Raiz quadrada de {numero} = {numero ** 0.5:.2f}")


numero = float(input("Digite um número: "))
tabuada(numero)
