#Uma empresa quer reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. 
#            Faça um programa que leia o salário atual, o género do funcionário e há quantos anos trabalha na empresa. 
#             No fim, mostre o novo salário, baseado na tabela a seguir:
#            - Mulheres
#              - menos de 15 anos de empresa: +5%
#              - de 15 até 20 anos de empresa: +12%
 #             - mais de 20 anos de empresa: +23%
  #          - Homens
#              - menos de 20 anos de empresa: +3%
#              - de 20 até 30 anos de empresa: +13%
#              - mais de 30 anos de empresa: +25%

nome = input('Qual é o nome do funcionário? ')
salario = float(input('Qual é o salário do funcionário? '))
tempo = int(input('Indique quantos anos está na empresa: '))
genero = int(input('Qual é o gênero do funcionário? [1] FEMININO [2] MASCULINO '))

if genero == 1:  # Feminino
    if tempo < 15:
        aumento = 0.05  # 5%
        novo_salario = salario + (salario * aumento)
    elif 15 <= tempo <= 20:
        aumento = 0.12  # 12%
        novo_salario = salario + (salario * aumento)

    else:
        aumento = 0.23  # 23%
        novo_salario = salario + (salario * aumento)
        
elif genero == 2:  # Masculino
    if tempo < 20:
        aumento = 0.03  # 3%
        novo_salario = salario + (salario * aumento)

    elif 20 <= tempo <= 30:
        aumento = 0.13  # 13%
        novo_salario = salario + (salario * aumento)

    else:
        aumento = 0.25  # 25%
        novo_salario = salario + (salario * aumento)
else:
    print("Opção de gênero inválida.")
    
print(f"O funcionário {nome} terá um aumento de {aumento*100:.0f}%.")
print(f"O novo salário será: R$ {novo_salario:.2f}")
