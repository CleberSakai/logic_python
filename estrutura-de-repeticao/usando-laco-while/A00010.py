nome = ''
while not nome:
    nome = input('Digite seu nome: ')
valor = int(input('Digite um número qualquer: '))
if valor:
    print('Você digitou um numero diferente de zero')
else:
    print('Você digitou zero.')