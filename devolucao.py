import json
from datetime import datetime
from livros import ler_livros, salvar_livros
from emprestimo import ler_emprestimos

def ler_devolucoes():
    lista_devolucoes = []
    try:
        with open('dados_devolucao.json', 'r') as file:
            lista_devolucoes = json.load(file)
        return lista_devolucoes
    except FileNotFoundError:
        print("Arquivo de devoluções ainda não existe!")
        return []

livros = ler_livros()

def atualizar_status_livro(titulo_livro, status_emprestimo):
    for livro in livros:
        if livro['titulo'].lower() == titulo_livro.lower():
            livro['emprestado'] = status_emprestimo
    salvar_livros(livros)

lista_devolucoes = ler_devolucoes()

def exibir_menu_devolucao():
    while True:
        print('---  SESSÃO DEVOLUÇÕES  ---')
        print('# --- 1)  Registrar Devolução --- #')
        print('# --- 2)  Listar Devoluções   --- #')
        print('# --- 0)  Salvar e Sair       --- #')
        try:
            opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))
        except ValueError:
            print('Opção inválida. Digite um número entre 0 e 2.')
            continue

        if opcao == 0:
            salvar_devolucao(lista_devolucoes)
            salvar_livros(livros)
            print('Voltando... Todas as alterações salvas!')
            break
        elif opcao == 1:
            registrar_devolucao()
        elif opcao == 2:
            listar_devolucoes()
        else:
            print('Opção inválida. Digite um número entre 0 e 2.')

def registrar_devolucao():
    lista_emprestimos = ler_emprestimos()
    livros = ler_livros()

    if not lista_emprestimos:
        print("Nenhum empréstimo cadastrado.")

    print('--- REGISTRAR DEVOLUÇÃO ---')                            
    cliente_existente = False
    while cliente_existente == False:
        nome_cliente = input('Digite o nome do cliente (ou "sair" para cancelar): ')
        if nome_cliente.lower() == "sair":
            print("Registro de devolução cancelado.")
            return

        for emprestimo in lista_emprestimos:
            if emprestimo['cliente'].lower() == nome_cliente.lower() and not emprestimo['devolvido']:
                cliente_existente = True
                break
        if cliente_existente == False:
            print("Cliente não encontrado ou não possui empréstimos pendentes. Tente novamente.")

    livro_existente = False
    while not livro_existente:
        titulo_livro = input('Digite o título do livro (ou "sair" para cancelar): ')
        if titulo_livro.lower() == "sair":
            print("Registro de devolução cancelado.")
            return
        
        

        livro_encontrado = False

        for emprestimo in lista_emprestimos:
            if emprestimo['livro'].lower() == titulo_livro.lower() and not emprestimo['devolvido']:
                for livro in livros:
                    if livro['titulo'].lower() == titulo_livro.lower() and livro['emprestado']:
                        livro_encontrado = True
                        break
                if livro_encontrado:
                    livro_existente = True
                    break
        if not livro_existente:
            print("Livro não encontrado, não foi emprestado, ou já devolvido. Tente novamente.")

    nova_devolucao = {}
    nova_devolucao['cliente'] = nome_cliente
    nova_devolucao['livro'] = titulo_livro
    nova_devolucao['data_emprestimo'] = emprestimo['data_emprestimo']
    nova_devolucao['data_devolucao'] = datetime.now().strftime('%d/%m/%Y')
    nova_devolucao['devolvido'] = True

    atualizar_status_livro(titulo_livro, False)

    print(f"Cliente:    {nova_devolucao['cliente']}")
    print(f"Livro:      {nova_devolucao['livro']}")
    print(f"Empréstimo: {nova_devolucao['data_emprestimo']}")
    print(f"Devolução:  {nova_devolucao['data_devolucao']}")

    lista_devolucoes.append(nova_devolucao)
    print('Devolução registrada com sucesso!')

def listar_devolucoes():
    if len(lista_devolucoes) == 0:
        print("Nenhuma devolução realizada")
    else:
        for devolucao in lista_devolucoes:
            print('-------------------------')
            print(f'Nome:            {devolucao['cliente']}')
            print(f'Livro:           {devolucao['livro']}')
            print(f'Data Emprestimo: {devolucao['data_emprestimo']}')
            print(f'Data Devolucao:  {datetime.now().strftime('%d/%m/%Y')}')
            print(f'Status:          {'Devolvido'}')
            print()

def salvar_devolucao(lista_devolucao):
    with open('dados_devolucao.json', 'w') as file:
        json.dump(lista_devolucao, file, indent=4)