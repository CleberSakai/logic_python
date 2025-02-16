'''

Uma loja de departamentos está oferecendo diferentes formas
de pagamento, conforme opções listadas a seguir. Faça um
algoritmo que leia o valor total de uma compra e calcule
o valor do pagamento final de acordo com a opção escolhida.

se a escolha for por pagamento parcelado, calcule também
o valor de cada parcela. Ao final, apresente o valor total
da compra e o valor das parcelas.

Pagamento à vista – conceder desconto de 5%;
Pagamento em 3x – o valor não sofre alterações;
Pagamento em 5x – acréscimo de 2%;
Pagamento em 10x – acréscimo 8%.

'''

print('Pagamento: ')
print('1 - á vista')
print('2 - parcelamento em 3x')
print('3 - parcelamento em 5x')
print('4 - parcelamento em 10x')
print('Pressione outra tecla para sair')

op = int(input('Qual forma de pagamento deseja fazer? '))
valor = float(input('Qual o preço do produto? '))

if (op == 1): #á vista desconto de 5%
    valor_final = valor * 0.95
    print('Produto comprado á vista. Total a pagar: {}'. format(valor_final))
elif(op == 2):
  valor_final = valor
  parcela = valor_final / 3
  print('Produto parcelado em 3x. Total a pagar {}, valor da parcela {}'. format(valor_final, parcela))
elif(op == 3):
   valor_final = valor * 1.02
   parcela = valor_final / 5
   print('Produto parcelado em 5x. Total a pagar {}, valor da parcela {}'. format(valor_final, parcela))
elif(op == 4):
   valor_final = valor * 1.08
   parcela = valor_final / 10
   print('Produto parcelado em 10x. Total a pagar {}, valor da parcela {}'. format(valor_final, parcela))
else:
   print('Operação inválida')