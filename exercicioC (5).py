# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. 
#  Nesse caso, exiba o valor da multa, cobrando 5€ por cada Km acima da velocidade permitida.

velocidade = int(input('Qual é a velocidade do carro? '))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5

    print(f'Você foi multado por excesso de velocidade! O valor da multa é de {multa}€.')

else:
    print('Parabéns! Por favor não ultrapasse a velocidade máxima.')

