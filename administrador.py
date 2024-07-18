from cliente import ler_clientes
from livros import ler_livros
from emprestimo import ler_emprestimos


lista_clietes = ler_clientes()
lista_livros = ler_livros()
lista_emprestimos = ler_emprestimos()


def autenticacao():
    print('---  SESSÃO  ADMINISTRADOR  ---')
    print('---  Digite "sair" para Sair  ---')
    login = input("Login: ")
    if login.lower() == "sair":
        return False
    senha = input("Senha: ")
    if senha.lower =="sair":
        return False   
    if login == "admin" and senha == "admin":
        return True
    else:
        return False


def exibir_menu_administrador():

    while True:
        print('---  SESSÃO  ADMINISTRADOR  ---')
        print('# --- 1)  Relatório Geral                 --- #')
        print('# --- 2)  Número de Livros Cadastrados    --- #')
        print('# --- 3)  Número de Livros Disponíveis    --- #')
        print('# --- 4)  Número de Livros Emprestados    --- #')
        print('# --- 5)  Número de Clientes Cadastrados  --- #')
        print('# --- 6)  Empréstimos Realizados          --- #')
        print('# --- 0)  Voltar                          --- #')
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n')) 

        if opcao == 1:
            exibir_relatorio()
        elif opcao == 2:
            print('Número de Livros Cadastrados: ', len(lista_livros))  
        elif opcao == 3:
            print('Número de Livros Disponíves: ', qtd_livros_disponiveis())
            print()
            listar_livros_disponiveis()
        elif opcao == 4:
            print("Número de Livros Emprestados: ", qtd_livros_emprestados())
        elif opcao == 5:
            print("Número de Clientes Cadastrados: ", len(lista_clietes))
        elif opcao == 6:
            print('Número de Devoluções: ', qtd_devolucoes())
        elif opcao == 0:
            break

def listar_livros_disponiveis():
    livros_disponiveis = []
    for livro in lista_livros:
        if livro['emprestado'] == False:
            livros_disponiveis.append(livro)

    for livro in livros_disponiveis:
        print("----------------------------")
        print(f"Livro: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"ISBN:  {livro['isbn']}")

def qtd_livros_disponiveis():
    livros_disponiveis = []
    for livro in lista_livros:
        if livro['emprestado'] == False:
            livros_disponiveis.append(livro)

    return len(livros_disponiveis)

def qtd_livros_emprestados():
    livros_emprestados = []
    for livro in lista_livros:
        if livro['emprestado'] == True:
            livros_emprestados.append(livro)

    return len(livros_emprestados)

def qtd_devolucoes():
    devolucoes = []
    for emprestimo in lista_emprestimos:
        if emprestimo['devolvido'] == True:
            devolucoes.append(emprestimo)

    return len(devolucoes)
        

def exibir_relatorio():
    print('#--- Relatório Geral ---#')
    print(f"N. Livros Cadastrados:     {len(lista_livros)}")
    print(f"N. Livros Disponíveis:     {qtd_livros_disponiveis()}")
    print(f"N. Livros Emprestados:     {qtd_livros_emprestados()}")
    print(f"N. Clientes Cadastrados:   {len(lista_clietes)}")
    print(f"N. Devoluções:             {qtd_devolucoes()}")
    print()