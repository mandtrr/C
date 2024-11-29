#1. Faça um programa para calcular a soma dos N primeiros números naturais (1+2+3+...+N) em que N é um número introduzido pelo utilizador.

n = int(input('Digite um número: '))

soma = 0

for numero in range (1, n + 1):
    print(numero)
    soma = soma + numero

print(f'A soma dos primeiros {n} números é de {soma}!')