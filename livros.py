#menu livros

lista_livros =[]

def menu_livros():
    while True:
        print('---  SESSÃO LIVROS  ---')
        print('# --- 1)  Cadastrar livro --- #')
        print('# --- 2)  Atualizar livro --- #')
        print('# --- 3)  Remover livro   --- #')
        print('# --- 4)  Listar livro    --- #')
        print('# --- 0)  Voltar             --- #')
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))

        if opcao == 0:
            break
        elif opcao == 1:
            cadastrar_livros()  
        elif opcao == 3:
            remover_livro()
        elif opcao == 4:
            listar_livros()


def cadastrar_livros(): 
    
    print('---  CADASTRAR LIVROS---')
    dados_livros = {}      
    nome_do_livro = input('Digite o nome do livro:')
    autor = input('Digite o nome do autor: ')
    isbn = input('Digite o ISBN do livro:')
    dados_livros['nome_do_livro'] = nome_do_livro
    dados_livros['autor'] = autor
    dados_livros['ISBN'] = isbn
    print('Novo livro cadastratado com sucesso!')

    print("Dados do livros: ", dados_livros)
    lista_livros.append(dados_livros)

def listar_livros():
    if len(lista_livros) == 0:
        print("Nenhum livro Cadastrado")
    print(lista_livros)



def remover_livro():
    isbn = input('Digie o ISBN do livro para remove-lo:')
    for livro in lista_livros:
        if livro['ISBN'] == isbn:
            lista_livros.remove(livro)
            print(f'O {livro["nome_do_livro"]} foi removido com sucesso. ')
        else:
            print('Livro não existe!')


