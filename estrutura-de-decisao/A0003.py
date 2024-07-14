print('Escolha o que deseja comprar: ')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual a sua escolha? '))
qtd = int(input('Qual a quantidade? '))

if produto == 1:
    pagar = qtd * 2.3
    print('Você comprou {} Maças, total à pagar {}: '.format(qtd, pagar))
else:
    if produto == 2:
        pagar = qtd * 3.6
        print('Você comprou {} Laranjas, total à pagar {}: '.format(qtd, pagar))
    else:
        if produto == 3:
            pagar = qtd * 1.85
            print('Você comprou {} bananas, total à pagar {}: '.format(qtd, pagar))
        else:
            print('Produto inexistente')
          