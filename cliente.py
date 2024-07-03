lista_clientes = []



def exibir_menu_cliente():
    while True:
        print('---  SESSÃO CLIENTES  ---')
        print('# --- 1)  Cadastrar Cliente  --- #')
        print('# --- 2)  Atualizar Cliente  --- #')
        print('# --- 3)  Remover Cliente    --- #')
        print('# --- 4)  Listar Clientes    --- #')
        print('# --- 0)  Voltar             --- #')
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))

        if opcao == 0:
            break
        elif opcao == 1:
            cadastrar_cliente()
        elif opcao == 4:
            listar_clientes()


def cadastrar_cliente():
    print('---  CADASTRAR CLIENTE  ---')
    dados_cliente = {}
    nome = input('Digite o nome do Cliente: ')
    cpf = input('Digite o CPF do Cliente:')
    dados_cliente['nome'] = nome
    dados_cliente['cpf'] = cpf

    print("Dados do Cliente: ", dados_cliente)
    lista_clientes.append(dados_cliente)


def listar_clientes():
    print(lista_clientes)
