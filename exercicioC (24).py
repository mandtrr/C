#66) Escreva um programa que leia um número qualquer e mostre a tabuada desse número, usando a estrutura “para”.
#                  Ex: Digite um valor: 5
#                  5 x 1 = 5
#                  5 x 2 = 10
#                  5 x 3 = 15 ...

numero = int(input('Digite um número para saber a tabuada: '))
print('Tabuada:')
for tabuada in range(1,11):
    print(f'{numero} x {tabuada} = {numero * tabuada}')
