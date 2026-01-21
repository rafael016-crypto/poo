#Números pares

for num in range(1,51):
    if num%2 == 0:
        print(num)



#Numeros Ímpares
soma = 0
for numero in range(1,501,2):
    if numero%3 == 0:
        print(numero)
impares = soma+numero
print(f'A soma dos números ímpares múltiplos de três no intervalo de 1 a 500 é {impares}')
