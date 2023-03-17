
frase = str(input('Digite uma frase: ')).lower().strip()

frase = frase.replace('á', 'a')
frase = frase.replace('à', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('â', 'a')
frase = frase.replace('ä', 'a')

print('A letra A aparece', frase.count('a'), 'vez(es) na frase.')
print('A primeira letra A apareceu na posição', frase.find('a') + 1)
print('A última letra A apareceu na posição',
      frase.rfind('a') + 1 - frase.count(' '))
