#18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar. Assuma o voto a partir dos 18 anos.

nascimento = int(input('Digite o ano do nascimento: '))

idade = 2024 - nascimento

if idade >= 18:
    print (f'O cidadão tem {idade} anos! Já pode votar!')

else:
    print (f'O cidadão tem {idade} anos! Ainda não pode votar!')