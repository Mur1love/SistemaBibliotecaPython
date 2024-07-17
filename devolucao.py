import json
from cliente import ler_clientes
from livros import ler_livros
from emprestimo import ler_emprestimos

ler_clientes()
ler_emprestimos()
ler_livros()

lista_emprestimos = ler_emprestimos()

def exibir_menu_devolucao():
    
    while True:
        print('---  SESSÃO DEVOLUÇÃO  ---')
        print('# --- 1)  Realizar Devolução    --- #')
        print('# --- 2)  Devoluções Realizadas --- #')
        print('# --- 0)  Voltar e Salvar    --- #')
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))  

        if opcao == 1:
            print("Devoluções Realizadas")  
        elif opcao == 2:
            print("Devoluções Realizadas")
        elif opcao == 0:
            break
