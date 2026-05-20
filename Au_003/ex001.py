import os
escolha_cliente = 0

def iniciar_app():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')
def coletar_escolha(x):
    x = input('Escolha uma opção: ')
    if x == '1':
        print('Opção 1 - Cadastrar restaurante')
    elif x == '2':
        print('Opção 2 - Listar restaurante')
    elif x == '3':
        print('Opção 3 - Ativar restaurante')
    elif x == '4':
        print('Opção 4 - Sair')
        sair_menu()
    else:
        print('Opção inválida!')
        return x
def sair_menu():
    os.system('cls')
    print('Saindo do menu...')

    
iniciar_app()
coletar_escolha(escolha_cliente)

