
print('Rodoviária Viaje Bem!')

distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'Preço da passagem: R$ {preco :.2f}')
