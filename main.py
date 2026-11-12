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
                    "Crise nas Infinitas Terras / Crisis on Infinite Earths": [
                        {
                            "nome": "Crisis on Infinite Earths #1",
                            "nome_alt": "Crise nas Infinitas Terras #1",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "03/04/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #2",
                            "nome_alt": "Crise nas Infinitas Terras #2",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "01/05/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #3",
                            "nome_alt": "Crise nas Infinitas Terras #3",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "05/06/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #4",
                            "nome_alt": "Crise nas Infinitas Terras #4",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "03/07/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #5",
                            "nome_alt": "Crise nas Infinitas Terras #5",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "07/08/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #6",
                            "nome_at": "Crise nas Infinitas Terras #6",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "04/09/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #7",
                            "nome_alt": "Crise nas Infinitas Terras #7",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "02/10/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #8",
                            "nome_alt": "Crise nas Infinitas Terras #8",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "06/11/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #9",
                            "nome_alt": "Crise nas Infinitas Terras #9",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "04/12/1985",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #10",
                            "nome_alt": "Crise nas Infinitas Terras #10",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "01/01/1986",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #11",
                            "nome_alt": "Crise nas Infinitas Terras #11",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "05/02/1986",
                            "precos": None,
                        },

                        {
                            "nome": "Crisis on Infinite Earths #12",
                            "nome_alt": "Crise nas Infinitas Terras #12",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": "05/03/1986",
                            "precos": None
                        }
                    ]
                }
            }
        }
    }

    return dados

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

def showStock():
    dados = openFile()
    estoque = dados["loja_info"]["estoque"]

    print("################### Coleção de obras ####################\n")

    for editora, saga in estoque.items():
        print(f"\n################### {editora} ###################")

        for nome_saga, quadrinhos in saga.items():
            print(f"\n################### {saga} ###################")

            for quadrinho in quadrinhos:
                print(f"{quadrinho["nome"]} - {quadrinho["autores"]}")
    
    return


def comicValidation(comic):

    dados = openFile()
    estoque = dados["loja_info"]["estoque"]

    for editora, colecoes in estoque.items():

        for nome_colecao, quadrinhos in colecoes.items():

            for quadrinho in quadrinhos:

                nome_original = quadrinho["nome"].lower()
                nome_alternativo = quadrinho.get("nome_alt", "").lower()

                if comic.lower() == nome_original or comic.lower() == nome_alternativo:

                    return quadrinho

    return None


def searchSys():   
    showStock()

    comic = input("Essas são as opções de obra para leitura.\nDigite o nome da obra para ver seus detalhes: ")

    if comicValidation(comic):
        showComicDetails()

    return

def showComicDetails(comic):
    dados = openFile()
    estoque = dados["loja_info"]["estoque"]

    print("------ Detalhes do produto ------\n")
    
    print(f"Nome da Obra: {comic["nome"]}")
    print(f"Autor(s) da Obra: {comic["autores"]}")
    print(f"Desenhista(s) da Obra: {comic["desenhistas"]}")
    print(f"Data de lançamento da Obra: {comic["data"]}")
    print(f"Preço da Obra (USD/BRL): {comic["precos"]}")

    print("Para se dirigir à opção de compra digite [1]\nPara adicionar o item ao carrinho digite [2]\nPara voltar ao menu anterior digite [0]\n")
    opcao = ("O que deseja fazer?: ")

    if (opcao.isdigit()) or not(int(opcao) > 0 or int(opcao) < 3):
        print("Por favor tente novamente. Digite uma opção válida.")
        showComicDetails(comic)
    else:

        if int(opcao) == 1:
            buyMenu()
        elif int(opcao) == 2:
            print("Item adicionado com sucesso")

            redirect = ("Deseja ver seus itens no carrinho?(s/n): ")

            if redirect.lower() == 's':
                shoppingList()
            elif redirect.lower == '2':
                print("Entendido. Voltando à lista de obras")

                searchSys()

        elif int(opcao) == 0:
            searchSys()

    return

def main(): ##Função de inicialização
    try:
        with open('dados.json', 'r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        createFile()
    print("##################### Bem-vindo ao sistema de gerenciamento da AMALGAMA COMIX!####################\n")
    print("Digite 1 para: Cadastrar usuário")
    print("Digite 2 para: Realizar login")
    print("Digite 0 para: Sair")
    menu_inicial()

main()
