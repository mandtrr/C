#72.Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) 
#	um vetor numérico com 10 posições: 5 10 15 20 25 30 35 40 45 50 

numeros = []

for n in range(1,11):
    numeros.append(n*5)

print("Valores: ", *numeros)