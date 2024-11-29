#Apresente a soma dos primeiros 10 numeros inteiros positivos

cont = 1
soma = 0

while cont<=10:
    print(f'{cont}')
    soma = soma + cont
    cont = cont + 1
print(f'A soma dos primeiros 10 números inteiros positivos é de: {soma}')