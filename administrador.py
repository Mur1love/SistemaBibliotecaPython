def exibir_menu_administrador():
   
    
    while True:
        print('---  SESSÃO  ADMINISTRADOR  ---')
        print('# --- 1)  Quantidade De Livros Disponiveis  --- #')
        print('# --- 2)  Livros Disponívei --- #')
        print('# --- 3)  Emprestado Realizados  --- #')
        print('# --- 4)  Clientes Cadastrados  --- #')
        print('# --- 5)  Empréstimos Realizados   --- #')
        print('# --- 0)  Voltar    --- #')
        opcao = int(input('--- Digite o número correspondente para selecionar: --- \n')) 

        if opcao == 1:
            print("Quantidade De Livros Disponiveis") 
        elif opcao == 2:
            print("Livros Disponívei") 
        elif opcao == 3:
            print("Emprestado Realizados")
        elif opcao == 4:
            print("Clientes Cadastrados")
        elif opcao == 5:
            print("Empréstimos Realizados")
        elif opcao == 0:
            break
        

         

        