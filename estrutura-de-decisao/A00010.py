'''

Faça um algoritmo que receba três valores, representando
os lados de um triângulo fornecidos pelo usuário. 
Verifique se os valores formam um triângulo e classifique como:

A. Equilátero (Três lados iguais)

B. Isósceles (Dois lados iguais)

C. Escaleno (Três lados diferentes)

Lembre-se que, para formar um triangulo, nenhum dos lados
pode ser igual a zero e um lado não pode ser maior que a 
soma dos outros dois


'''

A = int(input('Digite o primeiro lado do triângulo: '))
B = int(input('Digite o segundo lado do triângulo: '))
C = int(input('Digite o terceiro lado do triângulo: '))

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        
        if A != B and A != C and B != C:
            print('Triângulo escaleno!')
        else:
            if A == B and B == C:
                print('Triângulo equilátero')
            else:
                print('Triângulo isósceles')
    else:
        print('Ao menos um dos valores indicados não serve para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não serve para formar um triângulo')