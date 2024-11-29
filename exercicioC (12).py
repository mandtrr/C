#28) Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². 
#               O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
#              - Abaixo de 100m² = TERRENO POPULAR
#              - Entre 100m² e 500m² = TERRENO MASTER
#              - Acima de 500m² = TERRENO VIP

largura = float(input('Qual é a largura do terreno? '))
comprimento = float(input('Qual é o comprimento do terreno? '))

area = comprimento * largura

if area < 100:
    print(f'O terreno tem {area} metros quadrados. Sua classificação é: TERRENO POPULAR.')
elif area > 500:
    print(f'O terreno tem {area} metros quadrados. Sua classificação é: TERRENO VIP.')
else:
    print(f'O terreno tem {area} metros quadrados. Sua classificação é: TERRENO MASTER.')