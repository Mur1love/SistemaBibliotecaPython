from cliente import *
from livros import *
from administrador import *
from emprestimo import *
from devolucao import *

def main():
    exibir_menu_principal()
             
def exibir_menu_principal():
    while True:
        print('--- SISTEMA DE BIBLIOTECA PYTHON  ---')
        print('# --- 1)  Clientes      --- #')
        print('# --- 2)  Livros        --- #')
        print('# --- 3)  Emprestimo    --- #')
        print('# --- 4)  Devolução     --- #')
        print('# --- 5)  Administrador --- #')
        print('# --- 0)  Sair          --- #')

        try:
            opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))
        except ValueError:
            print('Opção inválida. Digite um número entre 0 e 5.')
            continue

        if opcao > 5 or opcao < 0:
            print('Opção inválida. D1jigite uma opção entre 0 e 5.')
        elif opcao == 0:
            print('Saindo do sistema')
            break
        elif opcao == 1:
            exibir_menu_cliente()
        elif opcao == 2:
            exibir_menu_livros()
        elif opcao == 3:
            exibir_menu_emprestimo()
        elif opcao == 4:
            exibir_menu_devolucao()
        elif opcao == 5:
            if autenticacao() == True:
                exibir_menu_administrador()
            else:
                print("Credenciais Incorretas. Tente novamente.")


if __name__ == "__main__":
    main()