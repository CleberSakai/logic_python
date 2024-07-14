'''
Escreva um programa que pergunte  a quantidade de km
percorridos por um carro alugado pelo usuario, assim como a
quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabndo que o carro custa R$ 60  por
dia e R$ 0,15% por km rodado
'''

'''



primeiro, quero pegar informações com o usuario.

Depois calcular o resultado e exibi-lo na tela

Mostrar o calculo pronto para o usuario e exibir o resultado.

input quantidade de km percorridos 

dias = quantidade de dias * 60
kms = quantidade de km * 0,15

total = dias + kms

input quantidade de dias  



'''
dias = int(input('Digite a quantidade de dias: '))
km = int(input('Digite os Km percorridos: '))

preco = 60 * dias + 0.15 * km

print('Foram pecorridos {}km, durante {} dias então o valor final é R${}' .format(km, dias, preco))
