
num = int(input('Digite um número entre 0 a 9999: '))
num += 10000
n = str(num).strip()

print(f'Unidade: {n[4]}')
print(f'Dezena: {n[3]}')
print(f'Centena: {n[2]}')
print(f'Milhar: {n[1]}')

# Utilizando matemática

'''
num = int(input('Digite um número entre 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Mihar: {milhar}')

'''
