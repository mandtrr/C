#Crie um programa que leia duas notas de um aluno e calcule a sua média,
 #             mostrando uma mensagem no final, de acordo com a média atingida:
#              - Média até 8.9: REPROVADO
#              - Média entre 9.0 e 10.9: RECUPERAÇÃO
#              - Média 11 ou superior: APROVADO

nome = input('Digite o nome do aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media >= 11:
    print(f'O aluno(a) {nome}, tem as notas {n1} e {n2}, a média é {media}.')
    print('O aluno(a) está aprovado!')

elif media <= 8.9:
    print(f'O aluno(a) {nome}, tem as notas {n1} e {n2}, a média é {media}.')
    print('O aluno(a) está reprovado!')

else:
    print(f'O aluno(a) {nome}, tem as notas {n1} e {n2}, a média é {media}.')
    print('O aluno(a) está rem recuperação!') 