import json

def ler_clientes():
    lista_clientes = []
    try:
        with open('dados_clientes.json', 'r') as file:
            lista_clientes = json.load(file)
        return lista_clientes
    except FileNotFoundError:
        print("Arquivo clientes ainda não existe!")


lista_clientes = ler_clientes()

def exibir_menu_cliente():
    
    while True:
        print('---  SESSÃO CLIENTES  ---')
        print('# --- 1)  Cadastrar Cliente  --- #')
        print('# --- 2)  Atualizar Cliente  --- #')
        print('# --- 3)  Remover Cliente    --- #')
        print('# --- 4)  Listar Clientes    --- #')
        print('# --- 5)  Buscar Clientes    --- #')
        print('# --- 0)  Voltar e Salvar    --- #')
        try:
            opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))
        except ValueError:
            print('Opção inválida. Digite um número entre 0 e 5.')
            continue 

        if opcao == 0:
            salvar_clientes(lista_clientes)
            print('Voltando... Todas as alterações salvas!')
            break
        elif opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            atualizar_cliente()    
        elif opcao == 3:
            remover_cliente()
        elif opcao == 4:
            listar_clientes()
        elif opcao == 5:
            buscar_clientes()


def cadastrar_cliente():
    print('---  CADASTRAR CLIENTE  ---')
    dados_cliente = {}      

    while True:
        nome = input('Digite o nome do Cliente: ')
        if len(nome) >= 3:
            break
        else:
            print('O nome deve ter no mínimo 3 caracteres.')

    while True:
        email = input('Digite o email do Cliente: ')
        if '@' in email:
            break
        else:
            print('O email deve conter "@".')

    cpf = input('Digite o CPF do Cliente: ')

    dados_cliente['nome'] = nome
    dados_cliente['email'] = email
    dados_cliente['cpf'] = cpf
    print('Novo cliente cadastratado com sucesso!')

    print("Os Dados do Cliente: ")
    print('Nome:  ', nome)
    print('E-mail: ', email)
    print('CPF:   ', cpf)
    lista_clientes.append(dados_cliente)
    print('Foram salvos com sucesso!')

def listar_clientes():
    if len(lista_clientes) == 0:
        print("Nenhum Cliente Cadastrado")
    else:
        for cliente in lista_clientes:
            print('---------------------------')
            print(f'Nome:   {cliente["nome"]}')
            print(f'E-mail: {cliente["email"]}')
            print(f'CPF:    {cliente["cpf"]}')
            print()

def buscar_clientes():
    nome_busca = input('Digite o nome do cliente que deseja buscar: ').lower()
    resultados = []
    
    for cliente in lista_clientes:
        if nome_busca in cliente['nome'].lower():
            resultados.append(cliente)
    
    if resultados:
        for cliente in resultados:
            print('---------------------------')
            print(f'Nome:   {cliente["nome"]}')
            print(f'E-mail: {cliente["email"]}')
            print(f'CPF:    {cliente["cpf"]}')
            print()
    else:
        print("Nenhum cliente encontrado com esse nome!")

def atualizar_cliente():
    cpf = input('Digite o CPF do cliente que deseja atualizar (Digite um número para cancelar):')
    if len(cpf) > 1: 
        achou = False
        for cliente in lista_clientes:
            if cliente['cpf'] == cpf:
                achou = True
                nome = input(f'Atualize o nome do Cliente (atual: {cliente["nome"]}): ')
                email = input(f'Atualize o email do Cliente (atual: {cliente["email"]}): ')

                cliente['nome'] = nome
                cliente['email'] = email
                print('Informações atualizadas com sucesso!')
                print(f'Nome: {cliente["nome"]}')
                print(f'E-Mail: {cliente["email"]}')
        if achou == False:
            print("CPF não encontrado, digite novamente!")
            atualizar_cliente()
    

def remover_cliente():
    cpf = input('Digie o CPF do cliente para remove-lo:')
    achou = False
    for cliente in lista_clientes:
        if cliente['cpf'] == cpf:
            lista_clientes.remove(cliente)
            achou = True
            print(f'O {cliente["nome"]} foi removido com sucesso. ')
    if achou == False:
        print('Cliente não existe!')


def salvar_clientes(lista_clientes):
    with open('dados_clientes.json', 'w') as file:
        json.dump(lista_clientes, file, indent = 4)


        