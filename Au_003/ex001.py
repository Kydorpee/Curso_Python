import os

restaurantes = []

# Funçoes cabecario
def exibir_funcao(texto):
    os.system('cls')
    print(f'{texto}:\n')
def retornar_menu():
    input("Pressione enter para retornar ao menu principal...")
    main()

# Funçoes principais
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
    os.system('cls')
    input('Opção inválida! pressione enter para tentar novamente...')
    main()
def cadastrar_restaurante():
    try:
        exibir_funcao("Cadastro de restaurante")

        nome = input('Digite o nome do restaurante: ')
        nome = nome.upper()
        categoria = input('Digite a categoria do restaurante: ')
        categoria = categoria.upper()

        dados_novo_restaurante = {'NOME':nome,'CATEGORIA':categoria,'STATUS':False}

        restaurantes.append(dados_novo_restaurante)

        print(f'O {nome} foi cadastrado com sucesso!\n')
        retornar_menu()

    except:
        print('Ocorreu um erro ao cadastrar o restaurante. Tente novamente.')
        input('Pressione enter para voltar ao menu...')
        main()
def listar_restaurantes():

    exibir_funcao("Lista de restaurantes")

    for item in restaurantes:

        nome = item['NOME']
        categoria = item['CATEGORIA']
        status = item['STATUS']

        print(f'- {nome} | {categoria} | {status}\n')

    retornar_menu()

def alterar_status():

    exibir_funcao("Alteração status")

    nome_restaurante = input('Digite o nome do restaurante para alterar o status: ')
    nome_restaurante = nome_restaurante.upper()
   
    for item in restaurantes:
        if item['NOME'] == nome_restaurante:
            item['STATUS'] = not item['STATUS']
            status_atualizado = 'Ativo' if item['STATUS'] else 'Inativo'
            print(f'O status do restaurante {nome_restaurante} foi alterado para {status_atualizado}.\n')
            break
    else:
        print(f'Não foi encontrado um restaurante com o nome {nome_restaurante}.\n')

    retornar_menu()

def coletar_escolha():
    try:
        x = input('Escolha uma opção: ')
        
        if x == '1':
            cadastrar_restaurante()
        elif x == '2':
            listar_restaurantes()
        elif x == '3':
            alterar_status()
        elif x == '4':
            print('Opção 4 - Sair')
            sair_menu()
        else:
            opcao_invalida()
    except:
        opcao_invalida()  
def sair_menu():
    exibir_funcao("Saindo do menu")

    
def main():
    os.system('cls')
    iniciar_app()
    coletar_escolha()


if __name__ == '__main__':
    main()


   