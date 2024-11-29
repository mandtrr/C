#Escreva um programa que leia o valor inicial da contagem, o valor final e o incremento. e mostre todos os valores do intervalo

inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
incremento = int(input("Digite o valor do incremento: "))

if incremento == 0:
    print("O incremento não pode ser zero.")
else:
    # Exibe os valores do intervalo na mesma linha
    for valor in range(inicial, final + 1, incremento):
        print(f"{valor} ", end="")  # Não pula linha