#9. Crie um vetor de 5 elementos. Escreva um programa que peça um número ao utilizador. 
#	Mostre uma mensagem dizendo se o número pedido ao utilizador e encontra no vetor.

numeros = [1, 2, 3, 4, 5]

elementos = int(input('Digite um número: '))

if elementos in numeros:
    print('O número inserido está no vetor!!')
else:
    print('O número inserido não está no vetor!')

