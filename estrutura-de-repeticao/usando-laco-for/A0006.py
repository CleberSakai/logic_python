'''

Escreva um algortimo que obtenha do usuario uma frase de 
tamanho entre 10 e 30 caracteres

'''

frase = input('Digite uma frase: ')
tamanho = len(frase)
while ((tamanho < 10) or (tamanho < 30)):
    frase = input('Digite uma frase')
    tamanho = len(frase)
print('Com espaços: {}'.format(frase))
print('Sem espaços: ', end='')
for i in range(0, tamanho, 1):
    if(frase[i] != ''):
        print(frase[i], end='')