#29) Desenvolva um programa que leia o nome de um funcionário, o seu salário, há quantos anos trabalha 
#             na empresa e mostre o seu novo salário, reajustado de acordo com a tabela a seguir:
#            - Até 3 anos de empresa: aumento de 3%
#            - entre 3 e 10 anos: aumento de 12.5%
#            - 10 anos ou mais: aumento de 20% 


nome = input('Qual é o nome do funcionário? ')
salario = float(input('Qual é o salário do funcionário? '))
tempo = int(input('Indique quantos anos está na empresa: '))

if tempo < 3:
    aumento = salario * (3 / 100)
    salario_atualizado = salario + aumento
    print(f'O funcionário {nome} trabalha na empresa há {tempo} anos, por isso receberá um aumento de 3% e seu salário será {salario_atualizado}€')

elif tempo >= 10:
    aumento = salario * (20 / 100)
    salario_atualizado = salario + aumento
    print(f'O funcionário {nome} trabalha na empresa há {tempo} anos, por isso receberá um aumento de 20% e seu salário será {salario_atualizado}€')

else:
    aumento = salario * (12.5 / 100)
    salario_atualizado = salario + aumento
    print(f'O funcionário {nome} trabalha na empresa há {tempo} anos, por isso receberá um aumento de 12.5% e seu salário será {salario_atualizado}€')
