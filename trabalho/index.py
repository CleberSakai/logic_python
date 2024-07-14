# Aqui será executada a mensagem de boas-vindas
print('Boas-vindas usuário, ao aplicativo de Cleberson Rodrigues dos Santos | RU: 4677966')

# Pedido para o cliente digitar o valor unitário de seu produto
valor_unitario = float(input('Qual o valor unitário do produto? '))

# Pedido para o cliente digitar a quantidade desejada do produto
quantidade = int(input('Digite a quantidade desejada: '))

# Aqui estou declarando o valor final do pedido que é o valor unitário * a quantidade selecionada
valor_total = valor_unitario * quantidade

# Para utilizar essa variavél fora da condicional, declarei ela aqui
valor_com_desconto = 0

# Para utilizar essa variavél fora da condicional, declarei ela aqui
desconto = 0


# Aplicação dos descontos

if (valor_total < 2500):
    print('Nessa compra não será aplicado nenhum desconto.')
elif (valor_total >= 2500 and valor_total < 6000):
    desconto = 4
    valor_do_desconto = valor_total * (desconto / 100)
    valor_com_desconto = valor_total - valor_do_desconto
elif (valor_total >= 6000 and valor_total < 10000):
    desconto = 7
    valor_do_desconto = valor_total * (desconto / 100)
    valor_com_desconto = valor_total - valor_do_desconto
else:
    desconto = 11
    valor_do_desconto = valor_total * (desconto / 100)
    valor_com_desconto = valor_total - valor_do_desconto
    

# Essas mensagens só serão printadas, caso o valor com desconto seja maior que zero
if valor_com_desconto > 0:
    print('O valor sem desconto foi de {}'.format(valor_total))
    print('O valor com desconto foi de {}. ( Desconto de {}% )'.format(valor_com_desconto, desconto))

