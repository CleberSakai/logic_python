'''

Escreva um algoritmo que repetidamente pergunte ao usuário qual sua idade e seu sexo (M ou F). Para cada resposta o programa deve responder imprimir a mensagem: "Boa noite, Senhor sua idade é <idade>"

'''

idade = int(input('Qual a sua idade? '))
while (idade > 0):
    sexo = input('Qual seu sexo? (M ou F)')
    if ((sexo == 'M') or (sexo == 'm')):
        print('Noa noite Senhor, sua idade é {}.'.format(idade))
    else:
     if((sexo == 'F') or (sexo == 'f')):
        print('Boa noite senhora, sua idade é {}.'.format(idade))
     else:
        print('Opção de sexo inexistente.')
idade = int(input('Qual sua idade?'))
print('encerrando....')