from cliente import *
from livros import*

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
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n'))

        if opcao > 5 or opcao < 0:
            print('Opção inválida. D1jigite uma opção entre 0 e 5.')
        elif opcao == 0:
            print('Saindo do sistema')
            break
        elif opcao == 1:
            exibir_menu_cliente()
        elif opcao == 2:
            menu_livros()

if __name__ == "__main__":
    main()