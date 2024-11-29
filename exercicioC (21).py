#51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados. 

maior_preco = 0
menor_preco = float('inf')

for p in range (8):
    preco = float(input('Digite o preço do produto: '))

    if preco > maior_preco:
        maior_preco = preco
    if preco < menor_preco:
        menor_preco = preco

print(f'O maior preço digitado foi: {maior_preco}€')
print(f'O menor preço digitado foi: {menor_preco}€')