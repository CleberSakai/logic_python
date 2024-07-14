'''

Escreva um algoritmo que leia dois valores numéricos e que
pergunte ao usuario qual a operação ele deseja realizar
adição, subtração, multiplicação ou divisão
Exiba na tela o resultado da operação desejada

'''

print('Calculadora')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Pressione outra tecla pra sair')

op = input('Qual operação deseja fazer: ')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if(op == '+'):
    res = x + y 
    print('O resultado de {} + {} = {}' .format(x, y, res))
elif(op == '-'):
    res = x - y
    print('O resultado de {} - {} = {}' .format(x, y, res))
elif(op == '*'):
    res = x * y
    print('O resultado de {} * {} = {}' .format(x, y, res))
elif(op == '/'):
    res = x / y 
    print('O resultado de {} / {} = {}' .format(x, y, res))
else:
    print('Operação inválida!')