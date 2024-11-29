import random  # Importa a biblioteca para gerar números aleatórios

# Inicializa uma lista vazia
numeros = []

# Preenche a lista com 10 números aleatórios de 1 a 100
for i in range(10):
    numero = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    numeros.append(numero)  # Adiciona o número à lista

# Exibe os números na ordem em que foram inseridos
print("Números na ordem original:", ', '.join(map(str, numeros)))

# Exibe os números na ordem inversa
print("Números na ordem inversa:", ', '.join(map(str, numeros[::-1])))
