#1. Escreva um programa que preencha um vetor com 10 números aleatórios de 1 a 100. 
#	Mostre o resultado na ordem em que os números foram inseridos e na ordem inversa.

import random

numeros = []

for n in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)


print('Números na ordem original:', *numeros)
print("Números na ordem inversa:", *numeros[::-1])