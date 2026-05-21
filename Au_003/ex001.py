import os
restaurantes = ['PKS Lanches','123 LANXHES']

# Funçoes
def exibir_funcao(texto):
    os.system('cls')
    print(f'{texto}:\n')
def retornar_menu():
    input("Pressione enter para retornar ao menu principal...")
    main()
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
        exibir_funcao("Cadastro de restaurante")
        nome_restaurante = input('Digite o nome do restaurante: ')
        nome_restaurante = nome_restaurante.upper()

        restaurantes.append(nome_restaurante)

        print(f'O {nome_restaurante} foi cadastrado com sucesso!\n')
        retornar_menu()

    except:
        print('Ocorreu um erro ao cadastrar o restaurante. Tente novamente.')
        input('Pressione enter para voltar ao menu...')
        main()
def listar_restaurantes():
    exibir_funcao("Lista de restaurantes")
    for item in restaurantes:
        print(f'- {item}\n')
    retornar_menu()



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


   