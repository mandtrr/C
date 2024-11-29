#19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre-a. No final, analise a média e mostre se o aluno teve ou não 
# um bom aproveitamento (se ficou acima da média 14.0/20).

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 14:
    print(f'O aluno(a) {nome}, tem as notas {nota1} e {nota2}, a média é {media}.')
    print('O aluno(a) teve um bom aproveitamento!')

else:
    print(f'O aluno(a) {nome}, tem as notas {nota1} e {nota2}, a média é {media}.')
    print('O aluno(a) está reprovado!')