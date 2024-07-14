tabuada = int(input('Digite o valor que deseja calcular a tabuada: '))
n = int(input('Digite até qual numero deseja mostrar a tabuada: '))
for i in range(1, n + 1, 1):
    print('{} x {} = {} '.format(tabuada, i, tabuada * i))
