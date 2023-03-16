frase = 'Isso é uma frase'
print(frase)

# Fatiamento
print(frase[3])  # imprimi a quarta letra da frase 'o'

print(frase[7:10])  # 'uma'

print(frase[:6])  # 'Isso é'

print(frase[7:])  # 'uma frase'

print(frase[0::2])  # imprime toda frase pulando de dois em dois

# Um parágrafo em um único print
print('''\nA tecnologia é o conjunto de conhecimentos e técnicas que envolvem a criação,
o desenvolvimento e a utilização de ferramentas, máquinas, equipamentos, sistemas e processos
que visam melhorar a qualidade de vida das pessoas e otimizar a realização de diversas atividades.
Nos dias de hoje, a tecnologia está cada vez mais presente em nossa rotina, seja por meio de dispositivos
móveis, sistemas inteligentes, internet das coisas, inteligência artificial, entre outras inovações.
Com o avanço contínuo da tecnologia, as possibilidades são infinitas e as soluções encontradas para diversos
problemas são cada vez mais rápidas e eficientes, o que transforma positivamente o mundo em que vivemos.\n''')

# Contagem
print(frase.count('a'))  # conta as letras a

# agora o método upper transforma a frase para maíscula e o count conta quantos 'A' tem
print(frase.upper().count('A'))

print(len(frase))  # exibe o tamanho da frase, incluindo os espaços.

frase = '     Isso é uma frase     '  # agora a frase possuí espaços extras

print(len(frase))  # contagem com os espaços extras

# método strip remove os espaços dos extremos, voltando a frase de origem.
print(len(frase.strip()))

frase = 'Isso é uma frase'

# imprimi a troca das palavras 'uma frase' por 'um texto'
print(frase.replace('uma frase', 'um texto'))
print(frase)  # não houve a troca, apenas na instância da linha 42

# para resolver, deve-se atribuir com o método replace.

frase = frase.replace('uma frase', 'um texto')
print(frase)

frase = 'Isso é uma frase'
print('Isso' in frase)  # checa se dentro da frase possui a str 'Isso'

print(frase.find('uma'))

# como o método não encontra a str dentro da frase, ele retorna -1
print(frase.find('isso'))

print(frase.lower().find('isso'))

print(frase.split(), '\n')  # retorna a str em lista

dividido = frase.split()  # cria uma lista com a variavel dividido
print(dividido)
print(dividido[1])  # mostra o segundo item da lista
print(dividido[3][2])  # retorna a letra 'a' do terceiro item da lista 'frase'
