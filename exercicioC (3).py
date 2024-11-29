#3. Escreva um algoritmo que leia um vetor de seis elementos numéricos inteiros. O algoritmo deverá calcular e mostrar:
#    a) a quantidade de números pares;
#    b) a quantidade de números ímpares.

numeros = []

for n in range(6):
    numero = int(input("Insira um número: "))
    numeros.append(numero)

#agora é o momento do contador, para contar os pares e ímpares e poder mostrar no print
par = 0
impar = 0

for numero in numeros:
    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print('Números: ', *numeros)
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')