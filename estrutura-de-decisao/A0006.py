nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if nome == 'Cleberson':
    print('Olá, Cleberson')
elif idade < 18:
    print('Você não é o Cleber! E é menor de idade')
elif idade > 100:
    print('Diferente de você, o Cleberson não é imortal')
