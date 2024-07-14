palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print('\nPalavra: {} Vogais: '.format(palavra), end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
