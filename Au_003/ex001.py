import os
restaurantes = []

# Funçoes

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
def opcao_invalida():
    input('Opção inválida! pressione enter para tentar novamente...')
    main()
def cadastrar_restaurante():
    try:
        os.system('cls')
        print('Cadastrar restaurante:\n')
        nome_restaurante = input('Digite o nome do restaurante: ')
        restaurantes.append(nome_restaurante)
        print(f'O {nome_restaurante} foi cadastrado com sucesso!\n')
        input('Pressione enter para voltar ao menu...')
        main()
    except:
        print('Ocorreu um erro ao cadastrar o restaurante. Tente novamente.')
        input('Pressione enter para voltar ao menu...')
        main()
def listar_restaurantes():
    os.system('cls')
    print('Lista de restaurantes cadastrados:\n')
    for item in restaurantes:
        print(f'- {item}\n')
    input("Pressione enter para retornar ao menu principal...")
    main()



def coletar_escolha():
    try:
        x = input('Escolha uma opção: ')
        
        if x == '1':
            cadastrar_restaurante()
        elif x == '2':
            listar_restaurantes()
        elif x == '3':
            print('Opção 3 - Ativar restaurante')
        elif x == '4':
            print('Opção 4 - Sair')
            sair_menu()
        else:
            opcao_invalida()
    except:
        opcao_invalida()  
def sair_menu():
    os.system('cls')
    print('Saindo do menu...')

    
def main():
    os.system('cls')
    iniciar_app()
    coletar_escolha()


if __name__ == '__main__':
    main()


   