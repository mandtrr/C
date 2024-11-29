# Inicializa uma lista vazia
numeros = []

# Loop para pedir ao usuário para inserir um número 5 vezes
for i in range(5):
    numero = int(input(f"Insira um número: "))
    numeros.append(numero)  # Adiciona o número à lista

# Exibe a lista final
print("Os números inseridos foram:", ', '.join(map(str, numeros)))