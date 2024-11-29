#77. Faça um programa que peça 7 nomes de pessoas ao utilizador e guarde-os em um vetor. No final, mostre uma listagem 
#	com todos os nomes na ordem inversa daquela em que eles foram introduzidos */

nomes = []

for n in range(1,8):
    nome= input("Insira um nome:")
    nomes.append(nome)

print("Os nomes inseridos na ordem inversa são: ", *nomes[::-1])
