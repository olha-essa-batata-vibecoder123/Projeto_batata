import json ##Biblioteca para arquivos. (Banco de Dados).

def createFile(): ## Função para criar o arquivo (BD).
    dados = {
        "user_info": [],

        "user_info_admin": {
            "username" : "administrador",
            "senha" : "batatasvoadoras123"
        },
        "loja_info": {
            "estoque": {
                "hq": None,
                "autor": None,
                "data": None
            },
            "carrinho": {
                "usuario": {
                    "hqs_selecionados": None
                }
            }
        }
    }

    with open('dados.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file)

    return

def openFile(): ## Função para abrir o arquivo (Acessar o BD).
    with open('dados.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

def signUp(): ##Função para cadastrar um novo usuário
    print("Cadastro de usuário")
    nome = input("Digite seu nome completo: ")
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    dados = openFile()

    if username == dados["user_info_admin"]["username"] and senha == dados["user_info_admin"]["senha"]:
        print("Bem-vindo ao menu de administrador")
        menu_admin()
        return
        
    for user in dados["user_info"]:
        if (username == user["username"] and senha == user["senha"]):
            print("Nome de usuário já cadastrado. Tente novamente.")
            signUp()

    new_user = {
        "nome": nome,
        "username": username,
        "senha": senha
    }
    dados["user_info"].append(new_user)

    with open('dados.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file)

    print("Cadastro realizado com sucesso!\nIniciando menu principal")
    menu_compras()

    return

def logIn(): ##Função para realizar login.
    print("Login de usuário")
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    dados = openFile()
    for user in dados["user_info"]:
        if (username == user["username"] and senha == user["senha"]):
            print("Login realizado com sucesso!\nBem-vindo(a), {}!".format(user["nome"]))
            return
    print("Nome de usuário ou senha incorretos. Tente novamente.")
    logIn()

    return

def menu_inicial(): ##Função do menu principal. Todas as outras opções e funções são executadas a partir daqui.
    print("Bem-vindo ao sistema de gerenciamento da AMALGAMA COMIX!")
    print("Digite 1 para: Cadastrar usuário")
    print("Digite 2 para: Realizar login")
    print("Digite 0 para: Sair")
    
    value = input("Escolha uma opção: ")

    if (not value.isdigit()) or (int(value) not in [0, 1, 2]):
        print("Opção inválida. Por favor, digite uma entrada válida (0, 1 ou 2).")
        menu_inicial()
    else:
        value = int(value)
        if value == 1:
            signUp()
        elif value == 2:
            logIn()
        elif value == 0:
            print("Encerrando o sistema. Até a próxima leitura!")
    return

def menu_compras():
    return 0

def menu_admin():
    return 0

def main(): ##Função de inicialização
    try:
        with open('dados.json', 'r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        createFile()
    menu_inicial()

main()##Inicialização.
