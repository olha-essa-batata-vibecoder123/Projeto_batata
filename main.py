import json ##Biblioteca para arquivos. (Banco de Dados).

def createFile(): ## Função para criar o arquivo (BD).
    dados = {
        "user_info": {
            "nome": None,
            "senha": None,
            "username": None
        },
        "user_info_admin": {
            "nome" : "administrador",
            "senha" : "batatasvoadoras123",
            "username" : "admin_loja"
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

def openFile(): ## Função para abrir o arquivo (Acessar o BD).
    with open('dados.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

def signUp(): ##Função para cadastrar um novo usuário
    print("Cadastro de usuário")
    nome = input("Digite seu nome: ")
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    dados = openFile()
    dados["user_info"]["nome"] = nome.lower()
    dados["user_info"]["username"] = username
    dados["user_info"]["senha"] = senha

    with open('dados.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file)

    print("Cadastro realizado com sucesso!\nRetornando ao menu principal...")
    menu()

def logIn(): ##Função para realizar login.
    print("Login de usuário")
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    dados = openFile()
    if username == dados["user_info"]["username"] and senha == dados["user_info"]["senha"]:
        print("Login realizado com sucesso!\nBem-vindo(a), {}!".format(dados["user_info"]["nome"]))
    else:
        print("Nome de usuário ou senha incorretos. Tente novamente.")
        logIn()

def menu(): ##Função do menu principal. Todas as outras opções e funções são executadas a partir daqui.
    print("Bem-vindo ao sistema de gerenciamento da AMALGAMA COMIX!")
    print("Digite 1 para: Cadastrar usuário")
    print("Digite 2 para: Realizar login")
    print("Digite 0 para: Sair")
    
    input = input("Escolha uma opção: ")

    if ((not input.isdigit()) or (int(input) not in [0, 1, 2])):
        print("Opção inválida. Por favor, digite uma entrada válida (0, 1 ou 2).")
        menu()
    else:
        input = int(input)
        if input == 1:
            signUp()
        elif input == 2:
            logIn()
        elif input == 0:
            print("Encerrando o sistema. Até a próxima leitura!")
def main(): ##Função principal do programa. O kickstart de tudo.
    if not openFile():
        createFile()
    menu()

main()##Boot up.