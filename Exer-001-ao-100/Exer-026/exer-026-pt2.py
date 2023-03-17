from unidecode import unidecode  # bibliteca para remover os acentos

frase = str(input('Digite uma frase: ')).lower().strip()
letra = str(input('Qual letra deseja procurar na frase? ')).lower().strip()
frase = unidecode(frase)

print(f'\nA letra {letra} aparece', frase.count(letra), 'vez(es) na frase.')
print(f'A primeira letra {letra} apareceu na posição', frase.find(letra) + 1)
print(f'A última letra {letra} apareceu na posição',
      frase.rfind(letra) + 1 - frase.count(' '))
