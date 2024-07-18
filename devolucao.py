import json
from cliente import ler_clientes
from livros import ler_livros, salvar_livros
from emprestimo import ler_emprestimos

ler_clientes()
ler_emprestimos()
livros = ler_livros()

def atualizar_status_livro(titulo_livro, status_emprestimo):
    for livro in livros:
        if livro['titulo'].lower() == titulo_livro.lower():
            livro['emprestado'] = status_emprestimo

lista_emprestimos = ler_emprestimos()

def exibir_menu_devolucao():
    
    while True:
        print('---  SESSÃO DEVOLUÇÃO  ---')
        print('# --- 1)  Realizar Devolução    --- #')
        print('# --- 2)  Devoluções Realizadas --- #')
        print('# --- 0)  Voltar e Salvar       --- #')
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))  

        if opcao == 1:
            realizar_devolucao() 
        elif opcao == 2:
            listar_devolucoes()
        elif opcao == 0:
            salvar_emprestimos(lista_emprestimos)
            salvar_livros(livros)
            print('Voltando... Todas as alterações salvas!')
            break


def realizar_devolucao():
    print('---  REALIZAR DEVOLUÇÃO  ---')
    nome_cliente = input('Digite o nome do cliente: ')
    titulo_livro = input('Digite o título do livro: ')

    emprestimo_encontrado = False

    for emprestimo in lista_emprestimos:
        if emprestimo['cliente'].lower() == nome_cliente.lower() and emprestimo['livro'].lower() == titulo_livro.lower():
            emprestimo_encontrado = True
            if emprestimo['devolvido'] == True:
                print('Este livro já foi devolvido.')
            else:
                emprestimo['devolvido'] = True
                atualizar_status_livro(titulo_livro, False)
                print('Devolução realizada com sucesso!')

    if emprestimo_encontrado == False:
        print('Empréstimo não encontrado. Verifique o nome do cliente e o título do livro.')

def listar_devolucoes():
    print('---  DEVOLUÇÕES REALIZADAS  ---')
    devolucoes_realizadas = []
    for emprestimo in lista_emprestimos:
        if emprestimo['devolvido'] == True:
            devolucoes_realizadas.append(emprestimo)

    if len(devolucoes_realizadas) == 0:
        print('Nenhuma devolução realizada.')
    else:
        for devolucao in devolucoes_realizadas:
            print('---------------------------')
            print(f'Cliente:         {devolucao["cliente"]}')
            print(f'Livro:           {devolucao["livro"]}')
            print(f'Data Empréstimo: {devolucao["data_emprestimo"]}')
            print(f'Data Devolução:  {devolucao["data_devolucao"]}')
            if devolucao['devolvido'] == True:
                print(f'Status:          Devolvido')
            else:
                print(f'Status:          Emprestado')
            print()

def salvar_emprestimos(lista_emprestimos):
    with open('dados_emprestimos.json', 'w') as file:
        json.dump(lista_emprestimos, file, indent=4)