# Aqui será executada a mensagem de boas-vindas
print('Boas-vindas a Copiadora de Cleberson Rodrigues dos Santos | RU: 4677966 \n')


# Definindo a função para a escolha de serviço
def escolha_servico():
   print('Entre com o tipo de serviço desejado: ')
   print('DIG - Digitalização')
   print('ICO - Impressão Colorida')
   print('IPB - Impressão Preto e Branco')
   print('FOT - Fotocópia')
   return input('>> ').lower()

# Declarando minha função em uma variável de escopo global
servico = escolha_servico()

# Fazendo a validação da escolha do serviço
while (servico != 'dig' and servico != 'ico' and servico != 'ipn' and servico != 'fot' ):
   print('Escolha Inválida.\nEntre com o tipo de serviço desejado novamente.\n')
   servico = escolha_servico()
   continue

# Definindo a função para o numéro de páginas selecionadas
def num_paginas():
   try:
    return int(input('Entre com o numéro de páginas: '))
   except:
      print('Valor inválido')

# Declarando minha função em uma variável de escopo global
paginas = num_paginas()

# Validação para o limite de numéros de páginas
while (paginas >= 20000):
   print('Não aceitamos tantas páginas de uma vez.')
   paginas = num_paginas()
   continue

# Definindo a função para a lista de serviços extras
def servico_extra():
   print('Deseja adicionar mais algum servico? ')
   print('1 - Encadernação Simples - R$ 15,00')
   print('2 - Encadernação Capa Dura - R$ 40,00')
   print('0 - Não Desejo Mais Nada')
   return input('>> ')

# Declarando minha função em uma variável de escopo global
extra = servico_extra()

# Fazendo validação da opção de serviço extra selecionada pelo usuário
while(extra != '1' and extra != '2' and extra != '0'):
   extra = servico_extra()
   continue

# Declarando dentro de um objeto os valores para cada tipo de serviço
preco_servicos = {
   'dig': 1.10,
   'ico': 1.00,
   'ipb': 0.40,
   'fot': 0.20,
} 

# usei o método get() para pegar o valor do serviço de dentro do meu objeto passando a key do serviço
valor_servico = preco_servicos.get(servico)

# Verificando qual será o desconto aplicado para a quantidade de páginas selecionadas
if(paginas < 20):
   print('Não Há Descontos')
elif(paginas >= 20 and paginas <200):
    paginas -= paginas * 0.15
elif(paginas >= 200 and paginas < 2000):
   paginas -= paginas * 0.20
elif(paginas >= 200 and paginas < 20000):
   paginas -= paginas * 0.25

# Declarando dentro de um objeto os valores para cada opção de serviço extra
preco_extras = {
    '0': 0,
    '1': 15,
    '2': 40,
}

# usei o método get() para pegar o valor do serviço extra de dentro do meu objeto passando a key do serviço extra selecionado
valor_servico_extra = preco_extras.get(extra)

# Convertendo os valores finais para numéros do tipo float
total = float(valor_servico * paginas + valor_servico_extra)

# Print que mostrará ao usuario o calculado efetuado
print('Total (R$): {} (servico: {} * paginas: {} + extras(s): {}) '.format(total, valor_servico, paginas, valor_servico_extra ))



   
   



    
    





