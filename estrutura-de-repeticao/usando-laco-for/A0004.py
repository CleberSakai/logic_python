'''

Escreva um algoritmo que econtre todos os numeros primos
de 2 ate 99, imprima na tela todos eles

'''

print('Primos de 2 até 99:')
for numero in range (2, 100, 1):
    #variavel que altera seu valor caso o num não seja primo
    flag = 0
    for i in range (2, numero, 1):
        #o num for divisivel qualquer valor, não é primo
        if(numero % i == 0):
            flag = 1
            #caso encontre um valor divisivel já faz um break,
            #assim não precisa testar até o final sem necessidade
            break
        if(not flag):
            print(numero)