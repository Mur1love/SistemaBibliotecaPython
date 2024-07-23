import json

def ler_livros():
    try:
        with open('dados_livros.json', 'r') as file:
            lista_livros = json.load(file)
        return lista_livros
    except FileNotFoundError:
        print("Arquivo de livros ainda não existe!")

def exibir_menu_livros():
    lista_livros = ler_livros()
    while True:
        print('---  SESSÃO LIVROS  ---')
        print('# --- 1)  Cadastrar livro --- #')
        print('# --- 2)  Atualizar livro --- #')
        print('# --- 3)  Remover livro   --- #')
        print('# --- 4)  Listar livros   --- #')
        print('# --- 5)  Buscar livros   --- #')
        print('# --- 0)  Voltar e Salvar --- #')
        try:
            opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))
        except ValueError:
            print('Opção inválida. Digite um número entre 0 e 5.')
            continue

        if opcao == 0:
            salvar_livros(lista_livros)
            print('Voltando... Todas as alterações salvas!')
            break
        elif opcao == 1:
            cadastrar_livros()  
        elif opcao == 2:
            atualizar_livro()
        elif opcao == 3:
            remover_livro()
        elif opcao == 4:
            listar_livros()
        elif opcao == 5:
            buscar_livros()


def cadastrar_livros(): 
    lista_livros = ler_livros()
    print('--- CADASTRAR LIVROS ---')
    dados_livro = {}      
    titulo = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor: ')
    isbn = input('Digite o ISBN do livro: ')
    dados_livro['titulo'] = titulo
    dados_livro['autor'] = autor
    dados_livro['isbn'] = isbn
    dados_livro['emprestado'] = False
    print('Novo livro cadastratado com sucesso!')
    
    print("Os dados do livro: ")
    print('Título:  ',titulo)
    print('Autor:   ',autor)
    print('ISBN:    ',isbn)
    lista_livros.append(dados_livro)
    print('Foram salvos com sucesso! Salve para confirmar cadastro.')

def listar_livros():
    lista_livros = ler_livros()
    if len(lista_livros) == 0:
        print("Nenhum livro cadastrado")
    for livro in lista_livros:
            print('---------------------------')
            print(f'Título:   {livro["titulo"]}')
            print(f'Autor:    {livro["autor"]}')
            print(f'ISBN:     {livro["isbn"]}')
            if livro['emprestado'] == False:
                print("Status:   Disponível")
            else:
                print("Status:   Emprestado")
            print()

def buscar_livros():
    lista_livros = ler_livros()
    titulo_busca = input('Digite o titulo do livro que deseja buscar: ').lower()
    resultados = []
    
    
    for livro in lista_livros:
        if titulo_busca in livro['titulo'].lower():
            resultados.append(livro)
    
    if resultados:
        for livro in resultados:
            print('---------------------------')
            print(f'Título:   {livro["titulo"]}')
            print(f'Autor:    {livro["autor"]}')
            print(f'ISBN:     {livro["isbn"]}')
            print()
    else:
        print("Nenhum livro encontrado com esse título!")


def remover_livro():
    lista_livros = ler_livros()
    isbn = input('Digie o ISBN do livro para remove-lo:')
    achou = False
    for livro in lista_livros:
        if livro['isbn'] == isbn:
            lista_livros.remove(livro)
            achou = True
            print(f'O livro {livro["titulo"]} foi removido com sucesso. Salve para confirmar remoção.')
    if achou == False:
        print('Livro não existe!')


def atualizar_livro():
    lista_livros = ler_livros()
    isbn = input('Digite o ISBN do livro que deseja atualizar (Digite um número para cancelar):')
    if len(isbn) > 1: 
        achou = False
        for livro in lista_livros:
            if livro['isbn'] == isbn:
                achou = True
                titulo = input(f'Atualize o Titulo do Livro (atual: {livro["titulo"]}): ')
                autor = input(f'Atualize o Autor do Livro (atual: {livro["autor"]}): ')

                livro['titulo'] = titulo
                livro['autor'] = autor
                print('Informações atualizadas com sucesso! Salve para confirmar atualização')
                print(f'Título: {livro["titulo"]}')
                print(f'Autor: {livro["autor"]}')
        if achou == False:
            print("ISBN não encontrado, digite novamente!")
            atualizar_livro()


def salvar_livros(lista_livros):
     with open('dados_livros.json', 'w') as file:
        json.dump(lista_livros, file, indent = 4)



