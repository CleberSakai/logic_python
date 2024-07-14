#desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual
# Calcule a sua idade e apresente na tela

ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano_atual = int(input('Digite o ano em que estamos: '))

idade = ano_atual - ano_nasc
print('Você tem {} anos de idade' .format(idade));

if(idade >= 18):
    print('E é maior de idade!')