import math

# Função para calcular a área do círculo
def calcular_area_circulo(raio):
    return math.pi * raio * raio

# Solicita um valor positivo para o raio
raio = float(input("Digite o valor do raio: "))

# Enquanto o valor do raio for negativo, o programa pede novamente
while raio < 0:
    print("O valor do raio não pode ser negativo.")
    raio = float(input("Digite um valor positivo para o raio: "))

# Calcula a área com o valor válido do raio
area = calcular_area_circulo(raio)
print(f"A área do círculo com raio {raio} é: {area:.2f}")
