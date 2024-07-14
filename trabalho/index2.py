# Declarando a tabela de preços
tabela_de_precos = [
     ['P',  'R$ 9,00',  'R$ 11,00',],
     ['M',  'R$ 14,00',  'R$ 16,00',],
     ['G',  'R$ 18,00',  'R$ 20,00',],
]

# Aqui será executada a mensagem de boas-vindas
print('Boas-vindas a açaiteria de Cleberson Rodrigues dos Santos | RU: 4677966')

# Aqui será exibida a tabela de itens e preços para o cliente
print('----------------------Cardápio----------------------')
print('------ | Tamanho | Cupuaçu (CP) | Açai (AC) | ------')

# Aqui estou retirando para cada linha da minha tabela de preços, tamanho e o preço de cada item da lista
for linha in tabela_de_precos:
    tamanho, cp_preco, ac_preco = linha
    print ('------ |    ' + tamanho + '    |   ' + cp_preco + '   |  ' + ac_preco + ' | ------')

print('----------------------------------------------------')


# Declarando variaveis globais
valor_total = 0
fazendo_pedido = 's'


# Validação dos pedidos, relacionado a seu tamanho e valor
while (fazendo_pedido == 's'):

    sabor = str.upper(input('Digite o Sabor de sua preferência: (CP/AC): '))
    


    while (sabor != 'AC' and sabor != 'CP'):
        print('Sabor Invalido. Tente Novamente')
        sabor = str.upper(input('Digite o Sabor de sua preferência: (CP/AC): '))
        continue

    tamanho = str.upper(input('Digite o Tamanho (P/M/G): '))
    

    while(tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
        print('Tamanho Inválido. Tente Novamente')
        tamanho = str.upper(input('Digite o Tamanho (P/M/G): '))
        continue

    # Variavel de escopo local referente aos preços do produto
    preco_produto = 0

    if (sabor == 'AC'):
        if(tamanho == 'P'):
            preco_produto = 11
        elif(tamanho == 'M'):
            preco_produto = 16
        else:
            preco_produto = 20
        print('Você pediu um Açai no tamanho {}: R$ {}' .format(tamanho, preco_produto))

    if (sabor == 'CP'):
        if(tamanho == 'P'):
            preco_produto = 9
        elif(tamanho == 'M'):
            preco_produto = 14
        else:
            preco_produto = 18
        print('Você pediu Cupuaçu no tamanho {}: R$ {}' .format(tamanho, preco_produto))

     # validando se o cliente quer continuar adicionando mais pedidos
    fazendo_pedido = str.lower(input('Deseja adicionar mais alguma coisa? (s/ Digite outra tecla para sair) '))
    if (fazendo_pedido != 's'):
        valor_total += preco_produto
        break
    else:
        valor_total += preco_produto
        continue

# Print onde mostrará ao usuario o valor total final a ser pago.
print('O valor total a ser pago: {}' .format(valor_total))





    
