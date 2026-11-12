import json 

def createFile():
    dados = {
        "user_info": [],

        "user_info_admin": {
            "username": "administrador",
            "senha": "batatasvoadoras123"
        },

        "loja_info": {
            "estoque": {
                "DC Comics": {
                    "Crise nas Infinitas Terras": [
                        {
                            "nome": "Crise nas Infinitas Terras #1",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "03/04/1985"
                        },
                        
                        {
                            "nome": "Crise nas Infinitas Terras #2",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "01/05/1985"
                        },
                        
                        {
                            "nome": "Crise nas Infinitas Terras #3",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "05/06/1985"
                        },
                        
                        {
                            "nome": "Crise nas Infinitas Terras #4",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "03/07/1985"
                        },
                        
                        {
                            "nome": "Crise nas Infinitas Terras #5",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "07/08/1985"
                        },

                        {
                            "nome": "Crise nas Infinitas Terras #6",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "04/09/1985"
                        },

                        {
                            "nome": "Crise nas Infinitas Terras #7",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "02/10/1985"
                        },

                        {
                            "nome": "Crise nas Infinitas Terras #8",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "06/11/1985"
                        },

                        {
                            "nome": "Crise nas Infinitas Terras #9",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "04/12/1985"
                        },

                        {
                            "nome": "Crise nas Infinitas Terras #10",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "01/01/1986"
                        },

                        {
                            "nome": "Crise nas Infinitas Terras #11",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "05/02/1986"
                        },


                        {
                            "nome": "Crise nas Infinitas Terras #12",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "05/03/1986"
                        }         
                    ],
                    "The Dark Knight": []
                }
            }
        }
    }
    return

def openFile(): 
    with open('dados.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

def signUp(): 
    print("Cadastro de usuário")
    nome = input("Digite seu nome completo: ")
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    dados = openFile()

    if username == dados["user_info_admin"]["username"] and senha == dados["user_info_admin"]["senha"]:
        print("Bem-vindo ao menu de administrador!")
        menu_admin()
        return
        
    for user in dados["user_info"]:
        if username == user["username"]:
            print("Nome de usuário já cadastrado. Tente novamente.")
            signUp()

    new_user = {
        "nome": nome,
        "username": username,
        "senha": senha,
        "carrinho" : [] 
    }
    dados["user_info"].append(new_user)

    with open('dados.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file)

    print(f"Cadastro realizado com sucesso!\nBem-vindo(a), {user["nome"]}")
    menu_principal()

    return

def logIn(): 
    print("Login de usuário")
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    dados = openFile()
    for user in dados["user_info"]:
        if (username == user["username"] and senha == user["senha"]):
            print(f"Login realizado com sucesso!\nBem-vindo(a), {user["nome"]}!")
            return
    print("Nome de usuário ou senha incorretos. Tente novamente.")
    logIn()

    return

def menu_inicial():
    
    value = input("Escolha uma opção: ")

    if (not value.isdigit()) or (int(value) not in [0, 1, 2]):
        print("Opção inválida. Por favor, digite uma entrada válida (0, 1 ou 2): ")
        menu_inicial()
    else:
        value = int(value)
        if value == 1:
            signUp()
        elif value == 2:
            logIn()
        elif value == 0:
            print("Encerrando o sistema. Até a próxima leitura!")
            exit()
    return

def menu_principal():
    print("Você pode:\n[1]Pesquisar obras\n[2]Verificar o carrinho\n[3]Encerrar sessão(voltar ao menu inicial)\n[4]Sair do programa")

    value = input("Escolha uma opção: ")

    if (not value.isdigit()) or (int(value) not in [0, 1, 2, 3, 4]):
        print("Opção inválida. Por favor, digite uma entrada válida (0, 1 2, 3 ou 4): ")
        menu_principal()
    else:
        value = int(value)

        if value == 1:
            searchSys()
        elif value == 2:
            shoppingList()
        elif value == 3:
            menu_inicial()
        elif value == 4:
            exit()
    return 

def menu_admin():
    print("Você pode:\n[1]Verificar o estoque\n[2]Editar o estoque\n[3]Encerrar sessão(voltar ao menu inicial)\n[4]Sair do programa")

    value = input("Escolha uma opção: ")

    if (not value.isdigit()) or (int(value) not in [0, 1, 2, 3, 4]):
            print("Opção inválida. Por favor, digite uma entrada válida (0, 1, 2, 3 ou 4): ")
            menu_admin()
    else:
        value = int(value)

        if value == 1:
            stockCheck()
        elif value == 2:
            stockEditing()
        elif value ==3:
            menu_inicial()
        elif value == 4:
            exit()
    return 

def searchSys():
    dados = openFile()


def main(): ##Função de inicialização
    try:
        with open('dados.json', 'r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        createFile()
    print("Bem-vindo ao sistema de gerenciamento da AMALGAMA COMIX!")
    print("Digite 1 para: Cadastrar usuário")
    print("Digite 2 para: Realizar login")
    print("Digite 0 para: Sair")
    menu_inicial()

main()
