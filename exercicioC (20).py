#50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 100 e mostre na tela:
#                a) Quais foram os números sorteados
#                b) Quantos números estão acima de 5
#                c) Quantos números são divisíveis por 3


import random

num_sorteados = [random.randint(0,100) for _ in range(20)]
print('Números sorteados: ', num_sorteados)

acima_cinco = [num for num in num_sorteados if num > 5]
print(f'Quantidade de números acima de 5: {len(acima_cinco)}')

divisiveis_tres = [num for num in num_sorteados if num % 3 == 0]
print(f'Quantidade de números divisíveis por 3: {len(divisiveis_tres)}')