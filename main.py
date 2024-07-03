def main():
    opcao = 0
    while opcao != '6':
        menu_principal()
        opcao = input('--- Digite o número correspondente para selecionar: --- \n')





def menu_principal():
        print('--- SISTEMA DE BIBLIOTECA PYTHON  ---')
        print('# --- 1)  Clientes      --- #')
        print('# --- 2)  Livros        --- #')
        print('# --- 3)  Emprestimo    --- #')
        print('# --- 4)  Devolução     --- #')
        print('# --- 5)  Administrador --- #')
        print('# --- 6)  Sair          --- #')

if __name__ == "__main__":
    main()