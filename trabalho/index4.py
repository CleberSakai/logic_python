# Aqui será executada a mensagem de boas-vindas
print('Boas-vindas usuário, a estante virtual de Cleberson Rodrigues dos Santos | RU: 4677966\n')
print ('*' * 60)


#Declaração de variaveis de escopo global
lista_livro = [] 
id_global = 0
opcao_selecionada = None

#Função criada para formatar o retorno do print, da consulta dos livros
def formata_retorno(livros):
    if(len(livros)):
        for livro in livros:
            print('===> \nid: {} \nnome: {} \nautor: {} \neditora: {} \n====' .format(livro['id'], livro['nome'], livro['autor'], livro['editora']))
    else:
        print('Nenhum Livro Encontrado')
    
#Função criada para exibir o menu principal e solicitar a entrada do usuario
def menu():
    global opcao_selecionada
    print('-' * 23 + 'MENU PRINCIPAL' + '-' * 23)
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro')
    print('3 - Remover Livro')
    print('4 - Encerrar Programa')
    opcao_selecionada = int(input('>> '))


#Função criada para o usuario fornecer informações sobre o livro que deseja cadastrar
def cadastrar_livro(id):
    print('-' * 23 + 'MENU CADASTRAR LIVRO' + '-' * 23)
    print('id do livro {}'.format(id_global))
    nome_livro = input('Qual nome do livro que deseja cadastrar? ')
    nome_autor = input('Qual nome do autor do livro? ')
    nome_editora = input('Qual a editora do livro? ')
    dados = {
        'id': id, 'nome': nome_livro, 'autor': nome_autor, 'editora': nome_editora
    }
    lista_livro.append(dados)
    print('Livro Cadastrado! ')

    
#função criada para executar diferentes condicionais a partir da operação selecionada pelo usuario no menu consultar livro
def executar_operacao(operacao):
    if(operacao == '1'):
        formata_retorno(lista_livro)
        consultar_livro()
    elif(operacao == '2'):
        id = int(input('Qual ID você deseja consultar? '))
        livro_filtrado = [livro for livro in lista_livro if livro['id'] == id]
        formata_retorno(livro_filtrado)
        consultar_livro()
    elif(operacao == '3'):
        autor = input('Por qual Autor deseja consultar seu livro? ')
        livro_filtrados = [livro for livro in lista_livro if livro['autor'] == autor]
        formata_retorno(livro_filtrados)
        consultar_livro()
    elif(operacao == '4'):
         menu()
    else:
        print('Opção inválida')

#função criada para dar ao usuario as opções para consultar os livros que cadastrou
def consultar_livro():
    print('-' * 23 + 'MENU CONSULTAR LIVRO' + '-' * 23)
    print('Qual opção desejada? ')
    print('1 - Consultar Todos')
    print('2 - Consultar por ID')
    print('3 - Consultar por Autor')
    print('4 - Retornar ao Menu')
    return executar_operacao(input('>> '))
    
   


#função criada para o usuario remover um livro de sua preferencia, por ID do livro 
def remover_livro():
    global lista_livro
    print('-' * 23 + 'MENU REMOVER LIVRO' + '-' * 23)
    id = int(input('Digite o id do livro a ser removido: '))
    lista_livro = [livro for livro in lista_livro if livro['id'] != id]
    print('Livro excluido da Lista!')

menu()

#Estrutura de repetição para cada opção selecionada do usuario no menu principal , em cada opcao selecionada, é chamada uma função diferente, que representa os diferentes menus
while(opcao_selecionada <= 4 and opcao_selecionada > 0):
    if(opcao_selecionada == 1):
        id_global += 1
        cadastrar_livro(id_global)
    elif(opcao_selecionada == 2):
        consultar_livro()
    elif(opcao_selecionada == 3):
        remover_livro()
    if(opcao_selecionada < 4):
        menu()
        continue
    else:
        print('Encerrando programa...')
        break

        





    



















