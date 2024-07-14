"""

Uma empresa concedeu um bônus de 20% para todos seus funcionários
com mais de 5 anos na empresa. Todos os outros que não se
enquadram nessa categoria receberam uma bonificação de 10%
somente. Escreva um algoritmo que leia o salário do funcionário
e seu tempo de empresa, depois apresente a bonificação de cada
funcionário na tela.

"""

salario = float(input('Qual seu salário? '))
tempo_de_empresa = int(input('Qual seu tempo na empresa? '))
ano_atual = int(input('Em que ano estamos? '))
tempo = tempo_de_empresa - ano_atual

if (tempo >= 5):
    bonus = salario * 0.2
else:
    bonus = salario * 0.1
print('Você tem {} anos dentro da empresa' .format(tempo_de_empresa))
print('Seu salário é de {}.' .format(salario))
print('E sua bonificação é de {}.' .format(bonus))
print('Salário final {}. ' .format(salario + bonus))