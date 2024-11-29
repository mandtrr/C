# Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
#para todos, mas especialmente para as mulheres. Faça um programa que leia nome,
#sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
# - Homens têm 5% de desconto
#- Mulheres têm 13% de desconto

nome = input('Qual é o seu nome? ')
valor = float(input('Qual é o valor da sua compra? '))
sexo = int(input('Qual é o seu gênero? [1] FEMININO [2] MASCULINO '))

if sexo == 1:
    desconto = valor * (13 / 100)
    valor_atualizado = valor - desconto
    print(f'Olá, {nome}! O valor da sua compra é de {valor_atualizado}€, pois usufrui de um desconto de 13% por ser mulher.')

else:
    desconto = valor * (5 / 100)
    valor_atualizado = valor - desconto
    print(f'Olá, {nome}! O valor da sua compra é de {valor_atualizado}€, pois usufrui de um desconto de 5% por ser homem.')