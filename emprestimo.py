import json
from datetime import datetime, timedelta
from cliente import ler_clientes
from livros import ler_livros, salvar_livros

lista_emprestimos = []

def ler_emprestimos():
    lista_emprestimos = []
    try:
        with open('dados_emprestimos.json', 'r') as file:
            lista_emprestimos = json.load(file)
        return lista_emprestimos
    except FileNotFoundError:
        print("Arquivo de empréstimos ainda não existe!")

ler_clientes()

livros = ler_livros()

def atualizar_status_livro(titulo_livro, status_emprestimo):
    for livro in livros:
        if livro['titulo'].lower() == titulo_livro.lower():
            livro['emprestado'] = status_emprestimo

lista_emprestimos = ler_emprestimos()

def exibir_menu_emprestimo():
    while True:
        print('---  SESSÃO EMPRÉSTIMOS  ---')
        print('# --- 1)  Cadastrar Empréstimo --- #')
        print('# --- 2)  Listar Empréstimos   --- #')
        print('# --- 0)  Voltar e Salvar      --- #')
        try:
            opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))
        except ValueError:
            print('Opção inválida. Digite um número entre 0 e 2.')
            continue

        if opcao == 0:
            salvar_emprestimos(lista_emprestimos)
            salvar_livros(livros)
            print('Voltando... Todas as alterações salvas!')
            break
        elif opcao == 1:
            cadastrar_emprestimo()
        elif opcao == 2:
            listar_emprestimos()
        else:
            print('Opção inválida. Digite um número entre 0 e 2.')

def cadastrar_emprestimo():
    clientes = ler_clientes()
    livros = ler_livros()

    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre clientes antes de fazer um empréstimo.")

    if not livros:
        print("Nenhum livro cadastrado. Cadastre livros antes de fazer um empréstimo.")

    print('--- CADASTRAR EMPRÉSTIMO ---')
    cliente_existente = False
    while cliente_existente == False:
        nome_cliente = input('Digite o nome do cliente (ou "sair" para cancelar): ')
        if nome_cliente.lower() == "sair":
            print("Cadastro de empréstimo cancelado.")
            return

        for cliente in clientes:
            if cliente['nome'].lower() == nome_cliente.lower():
                cliente_existente = True
                break
        if cliente_existente == False:
            print("Cliente não encontrado. Tente novamente.")

    livro_existente = False
    while livro_existente == False:
        titulo_livro = input('Digite o título do livro (ou "sair" para cancelar): ')
        if titulo_livro.lower() == "sair":
            print("Cadastro de empréstimo cancelado.")
            return

        for livro in livros:
            if livro['titulo'].lower() == titulo_livro.lower():
                livro_existente = True
                break
        if livro_existente == False:
            print("Livro não encontrado. Tente novamente.")
        else:
            for livro in livros:
                if livro['titulo'].lower() == titulo_livro.lower() and livro['emprestado'] == True: 
                    print("Livro já está emprestado. Digite outro título ou 'sair' para cancelar.")
                    livro_existente = False
    


    novo_emprestimo = {}
    dias_emprestimo = 7
    data_emprestimo = datetime.now()
    data_devolucao = data_emprestimo + timedelta(days=dias_emprestimo)
    novo_emprestimo["cliente"] = nome_cliente
    novo_emprestimo["livro"] = titulo_livro
    novo_emprestimo["data_emprestimo"] = data_emprestimo.strftime('%d/%m/%Y')
    novo_emprestimo["data_devolucao"] = data_devolucao.strftime('%d/%m/%Y')
    novo_emprestimo["devolvido"] = False

    atualizar_status_livro(titulo_livro, True)

    print(f"Cliente:    {novo_emprestimo['cliente']}")
    print(f"Livro:      {novo_emprestimo['livro']}")
    print(f"Emprestimo: {novo_emprestimo['data_emprestimo']}")
    print(f"Devolução:  {novo_emprestimo['data_devolucao']}")

    lista_emprestimos.append(novo_emprestimo)
    print('Empréstimo cadastrado com sucesso!')

def listar_emprestimos():
    livros = ler_livros()
    lista_emprestados = []
    lista_emprestimos = ler_emprestimos()

    for emprestimo in lista_emprestimos:
        livro_correspondente = {}
        encontrou = False
        for livro in livros:
            if livro['titulo'].lower() == emprestimo['livro'].lower():
                livro_correspondente = livro
                encontrou = True
                break
        
        if encontrou == True and livro_correspondente['emprestado'] == True:
            lista_emprestados.append(emprestimo)

    if len(lista_emprestados) == 0:
        print("Nenhum empréstimo em andamento.")
    else:
        for emprestimo in lista_emprestados:
            print('---------------------------')
            print(f'Cliente:         {emprestimo["cliente"]}')
            print(f'Livro:           {emprestimo["livro"]}')
            print(f'Data Empréstimo: {emprestimo["data_emprestimo"]}')
            print(f'Data Devolução:  {emprestimo["data_devolucao"]}')
            print(f'Status:          Emprestado')
            print()

def salvar_emprestimos(lista_emprestimos):
    with open('dados_emprestimos.json', 'w') as file:
        json.dump(lista_emprestimos, file, indent=4)