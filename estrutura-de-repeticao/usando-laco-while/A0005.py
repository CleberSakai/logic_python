x = int(input('Digite um valor: '))
y = int(input('Digite um segundo valor: '))
cont = 1
multi = 0
while (cont <= x):
    multi += y
    cont += 1
print('Resultado da multiplicação: {}x{}={} '.format(x, y, multi))