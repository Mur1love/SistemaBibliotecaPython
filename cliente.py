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
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))    

        if opcao == 0:
            salvar_clientes(lista_clientes)
            print('Saindo... Todas as alterações salvas!')
            break
        elif opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            atualizar_cliente()    
        elif opcao == 3:
            remover_cliente()
        elif opcao == 4:
            listar_clientes()


def cadastrar_cliente():
    print('---  CADASTRAR CLIENTE  ---')
    dados_cliente = {}      
    nome = input('Digite o nome do Cliente: ')
    email = input('Digite o email do Cliente: ')
    cpf = input('Digite o CPF do Cliente:')
    dados_cliente['nome'] = nome
    dados_cliente['email'] = email
    dados_cliente['cpf'] = cpf
    print('Novo cliente cadastratado com sucesso!')

    print("Os Dados do Cliente: ")
    print('Nome:  ', nome)
    print('E-mal: ', email)
    print('CPF:   ', cpf)
    lista_clientes.append(dados_cliente)
    print('Foram salvos com sucesso!')

#Essa função não irá para a versão final pois apenas o ADM pode listar os clientes cadastrados
def listar_clientes():
    if len(lista_clientes) == 0:
        print("Nenhum Cliente Cadastrado")
    else:
        for cliente in lista_clientes:
            print('---------------------------')
            print(f'Nome:   {cliente['nome']}')
            print(f'E-mail: {cliente['email']}')
            print(f'CPF:    {cliente['cpf']}')
            print()

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
                print(f'Gmail: {cliente["email"]}')
        if achou == False:
            print("CPF não encontrado, digite novamente!")
            atualizar_cliente()
    

def remover_cliente():
    cpf = input('Digie o CPF do cliente para remove-lo:')
    for cliente in lista_clientes:
        if cliente['cpf'] == cpf:
            lista_clientes.remove(cliente)
            print(f'O {cliente['nome']} foi removido com sucesso. ')
        else:
            print('Cliente não existe!')


def salvar_clientes(lista_clientes):
    with open('dados_clientes.json', 'w') as file:
        json.dump(lista_clientes, file, indent = 4)


        