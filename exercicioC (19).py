#49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.

cont_pares = 0
cont_impar = 0

for contagem in range(6):
    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0:
        cont_pares = cont_pares + 1
    else:
        cont_impar = cont_impar + 1

print(f'Números pares: {cont_pares}')
print(f'Números ímpares: {cont_impar}')