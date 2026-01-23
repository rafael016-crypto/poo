import random
numero = random.randint (0,10)
numero_certo = 0
while numero_certo < 3:

    num = int(input("Digite um numero entre (0,10):"))
    if num == numero_certo:
        print ("Parabéns você acertou:")
        break
    numero_certo = numero_certo + 1
else:
    print("Você erro tente novamente")
----------------------------------------------------------------------
#Tabuada em while

numero = int(input("digite um numero"))
tabuada = 0
while tabuada<=10:
    resultado = numero * tabuada
    print (f"{numero} X {tabuada} = {resultado}")
    tabuada+=1
----------------------------------------------------------------------

while True:
    numero = int(input("digite um numero"))
    if numero <0:
        print("Progama encerrado. Obrigado!")
        break
    for i in range (1,10):
        resultado = numero * i
        print (f"{numero} X {i} = {resultado}")


--------------------------------------------------------------------
#Fatorial
numero = int(input("Digite um número: "))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador += 1

print(f"O fatorial de {numero} é {fatorial}")

-----------------------------------------------------------------

def area(largura, comprimento):
    return largura * comprimento

# Solicita as dimensões do terreno ao usuário
largura_terreno = float(input("Digite a largura do terreno: "))
comprimento_terreno = float(input("Digite o comprimento do terreno: "))

# Calcula a área utilizando a função area()
area_terreno = area(largura_terreno, comprimento_terreno)

# Exibe a área do terreno
print(f"A área do terreno é: {area_terreno} metros quadrados.")


       
