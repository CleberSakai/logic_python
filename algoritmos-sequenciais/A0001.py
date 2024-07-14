'''
a = 4
b = 6

c = a*a + b*b

'''

#s1 = 'ant'
#s2 = 'bat'
#s3= 'cod'

#print(s1 + ' '+  s2 + ' ' + s3)

#print(10 * (s1 + ' '))

#print( 1* (s1 + ' ') + 2*(s2 + ' ') + 3*(s3 + ' '))

#print((s1 +' ' + s2 + ' ') *7 )

#print((s1+s2+s3 + ' ') * 5)
 
'''
 Exercicio 1


Desenvolva um algoritmo que solicite ao usuario o preço
de um produto e um percentual de desconto a ser aplicado a ele
calcule e exiba o valor do desconto e o preço final

input preco
input desconto

total preco % desconto

print 
'''


preco = float(input('Digite o preço: '))
p = float(input('Digite o desconto a ser aplicado: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {} Desconto de {}%.' .format(preco, p))
print('O valor final é de: {}' .format(final))



