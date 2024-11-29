#24) Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando 0.8€ por Km para
# viagens até 200Km e 0.65€ para viagens mais longas.

distancia = float(input('Digite a distância que pretende percorrer em KM: '))

if distancia >= 200:
    passagem = distancia * 0.65
    print(f'Para {distancia}km, o valor da passagem será de {passagem}€.')

else:
    passagem = distancia * 0.80
    print(f'Para {distancia}km, o valor da passagem será de {passagem}€.')
