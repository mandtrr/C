#44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em #seguida    
#	todos os valores no intervalo:
#                                        Ex: Digite o primeiro Valor: 3
#                                        Digite o último Valor: 10
#                                        Digite o incremento: 2
#                                        Contagem: 3 5 7 9

primeiro_valor = int(input('Digite o primeiro valor: '))
ultimo_valor = int(input('Digite o último valor: '))
incremento = int(input('Digite o incremento: '))
print('Resultado:')
for n in range(primeiro_valor, ultimo_valor, incremento):
    print(n)
