while True:
    nome = input('Qual seu nome? ')
    if (nome != 'Cleber'):
        continue
    senha = input('Qual a sua senha?')
    if (senha == '123'):
        break
print('Acesso concedido')