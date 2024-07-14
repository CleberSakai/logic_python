'''

Crie uma variável de string que receba uma frase qualquer
Crie uma segunda variável, agora contendo a metade da string digitada
Imprima na tela somento os dois ultimos caracteres
da segunda variavel do tipo string

primeiro

preciso criar duas variaveis do tipo string
depois fazer a primeira com uma frase 
e a segunda com apenas metade da frase , e imprimir apenas
2 caracteres da segunda variavel

variaveis podem ser somente do tipo string

solucionar a questão e exibir o resultado na tela

variavel frase1
variavel frase2



'''

frase = input('Digite uma frase: ')
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])