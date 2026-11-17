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
                "Marvel Comics": {
                    "Weapon X": [
                        {
                            "nome": "Weapon X",
                            "nome_alt": "Arma X",
                            "autores": "Barry Windsor-Smith",
                            "desenhistas": "Barry Windsor-Smith",
                            "data": "1991",
                            "precos": None
                        },
                        {
                            "nome": "The Shiva Scenario",
                            "nome_alt": "O Cenário Shiva",
                            "autores": "Larry Hama",
                            "desenhistas": "Marc Silvestri",
                            "data": "1991–1992",
                            "precos": None
                        },
                        {
                            "nome": "Weapon X: The Draft – Wild Child",
                            "nome_alt": "Arma X: O Recrutamento – Selvagem",
                            "autores": "Frank Tieri",
                            "desenhistas": "Georges Jeanty",
                            "data": "2002",
                            "precos": None
                        },
                        {
                            "nome": "Weapon X",
                            "nome_alt": "Arma X",
                            "autores": "Greg Pak",
                            "desenhistas": "Greg Land e outros",
                            "data": "2017–2018",
                            "precos": None
                        }
                    ],

                    "Secret Wars": [
                        {
                            "nome": "Marvel Super Heroes: Secret Wars #1–12",
                            "nome_alt": "Super-Heróis Marvel: Guerras Secretas #1–12",
                            "autores": "Jim Shooter",
                            "desenhistas": "Mike Zeck",
                            "data": "1984–1985",
                            "precos": None
                        },
                        {
                            "nome": "Secret Wars II #1–9",
                            "nome_alt": "Guerras Secretas II #1–9",
                            "autores": "Jim Shooter",
                            "desenhistas": "Al Milgrom",
                            "data": "1985–1986",
                            "precos": None
                        },
                        {
                            "nome": "Secret Wars #1–9",
                            "nome_alt": "Guerras Secretas #1–9",
                            "autores": "Jonathan Hickman",
                            "desenhistas": "Esad Ribić",
                            "data": "2015–2016",
                            "precos": None
                        }
                    ],

                    "Civil War": [
                        {
                            "nome": "Civil War #1–7",
                            "nome_alt": "Guerra Civil #1–7",
                            "autores": "Mark Millar",
                            "desenhistas": "Steve McNiven",
                            "data": "2006–2007",
                            "precos": None
                        },
                        {
                            "nome": "Civil War: Front Line #1–11",
                            "nome_alt": "Guerra Civil: Linha de Frente #1–11",
                            "autores": "Paul Jenkins",
                            "desenhistas": "Ramon Bachs / Steve Lieber",
                            "data": "2006–2007",
                            "precos": None
                        },
                        {
                            "nome": "Civil War: The Confession",
                            "nome_alt": "Guerra Civil: A Confissão",
                            "autores": "Brian Michael Bendis",
                            "desenhistas": "Alex Maleev",
                            "data": "2007",
                            "precos": None
                        },
                        {
                            "nome": "Civil War: The Initiative",
                            "nome_alt": "Guerra Civil: A Iniciativa",
                            "autores": "Brian Michael Bendis / Warren Ellis",
                            "desenhistas": "Marc Silvestri",
                            "data": "2007",
                            "precos": None
                        }
                    ]
                },

                "DC Comics": {
                    "Crise nas Infinitas Terras / Crisis on Infinite Earths": [
                        {
                            "nome": f"Crisis on Infinite Earths #{i}",
                            "nome_alt": f"Crise nas Infinitas Terras #{i}",
                            "autores": "Marv Wolfman",
                            "desenhistas": "George Pérez",
                            "data": data,
                            "precos": None
                        }
                        for i, data in enumerate([
                            "03/04/1985",
                            "01/05/1985",
                            "05/06/1985",
                            "03/07/1985",
                            "07/08/1985",
                            "04/09/1985",
                            "02/10/1985",
                            "06/11/1985",
                            "04/12/1985",
                            "01/01/1986",
                            "05/02/1986",
                            "05/03/1986"
                        ], start=1)
                    ]
                }
            }
        }
    }

    return dados


def saveFile(dados):
    with open('dados.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)


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
            print("Nome de usuário já cadastrado.")
            return

    new_user = {
        "nome": nome,
        "username": username,
        "senha": senha,
        "carrinho": []
    }

    dados["user_info"].append(new_user)
    saveFile(dados)

    print(f"Cadastro realizado com sucesso!\nBem-vindo(a), {new_user['nome']}!")

    menu_principal(username)


def logIn():
    print("Login de usuário")

    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    dados = openFile()

    if username == dados["user_info_admin"]["username"] and senha == dados["user_info_admin"]["senha"]:
        print("Bem-vindo ao menu de administrador!")
        menu_admin()
        return

    for user in dados["user_info"]:
        if username == user["username"] and senha == user["senha"]:
            print(f"Login realizado com sucesso!\nBem-vindo(a), {user['nome']}!")
            menu_principal(username)
            return

    print("Nome de usuário ou senha incorretos.")
    menu_inicial()


def menu_inicial():
    print("\n################ MENU INICIAL ################")
    print("[1] Cadastrar usuário")
    print("[2] Realizar login")
    print("[0] Sair")

    value = input("Escolha uma opção: ")

    if value not in ["0", "1", "2"]:
        print("Opção inválida.")
        menu_inicial()

    elif value == "1":
        signUp()

    elif value == "2":
        logIn()

    elif value == "0":
        print("Encerrando o sistema. Até a próxima leitura!")


def menu_principal(username):
    print("\n################ MENU PRINCIPAL ################")
    print("[1] Pesquisar obras")
    print("[2] Verificar o carrinho")
    print("[3] Encerrar sessão")
    print("[4] Sair do programa")

    value = input("Escolha uma opção: ")

    if value == "1":
        searchSys(username)

    elif value == "2":
        shoppingList(username)

    elif value == "3":
        menu_inicial()

    elif value == "4":
        exit()

    else:
        print("Opção inválida.")
        menu_principal(username)


def menu_admin():
    print("\n################ MENU ADMINISTRADOR ################")
    print("[1] Verificar o estoque")
    print("[2] Editar o estoque")
    print("[3] Encerrar sessão")
    print("[4] Sair do programa")

    value = input("Escolha uma opção: ")

    if value == "1":
        stockCheck()

    elif value == "2":
        stockEditing()

    elif value == "3":
        menu_inicial()

    elif value == "4":
        exit()

    else:
        print("Opção inválida.")
        menu_admin()


def showStock():
    dados = openFile()
    estoque = dados["loja_info"]["estoque"]

    print("\n################### COLEÇÃO DE OBRAS ####################")

    for editora, colecoes in estoque.items():
        print(f"\n################### {editora} ###################")

        for nome_saga, quadrinhos in colecoes.items():
            print(f"\n################### {nome_saga} ###################")

            for quadrinho in quadrinhos:
                print(f"{quadrinho['nome']} - {quadrinho['autores']}")

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


def searchSys(username):
    showStock()

    comic = input("\nDigite o nome da obra para ver seus detalhes: ")

    resultado = comicValidation(comic)

    if resultado:
        showComicDetails(resultado, username)

    else:
        print("Obra não encontrada.")

    menu_principal(username)


def showComicDetails(comic, username):
    print("\n------ DETALHES DO PRODUTO ------")

    print(f"Nome da Obra: {comic['nome']}")
    print(f"Autor(es): {comic['autores']}")
    print(f"Desenhista(s): {comic['desenhistas']}")
    print(f"Data de lançamento: {comic['data']}")
    print(f"Preço da Obra (USD/BRL): {comic.get('precos', 'Não informado')}")

    print("\n[1] Comprar obra")
    print("[2] Adicionar item ao carrinho")
    print("[0] Voltar ao menu anterior")

    opcao = input("O que deseja fazer?: ")

    if opcao == "1":
        buyMenu(comic, username)

    elif opcao == "2":
        dados = openFile()

        for user in dados["user_info"]:
            if user["username"] == username:
                user["carrinho"].append(comic)
                saveFile(dados)
                print("Item adicionado ao carrinho com sucesso!")
                break

        redirect = input("Deseja ver seus itens no carrinho? (s/n): ")

        if redirect.lower() == "s":
            shoppingList(username)

        elif redirect.lower() == "n":
            searchSys(username)

        else:
            print("Opção inválida.")
            searchSys(username)

    elif opcao == "0":
        searchSys(username)

    else:
        print("Por favor, digite uma opção válida.")
        showComicDetails(comic, username)


def shoppingList(username):
    dados = openFile()

    for user in dados["user_info"]:
        if user["username"] == username:

            print("\n################### SEU CARRINHO ###################")

            if not user["carrinho"]:
                print("Seu carrinho está vazio.")

            else:
                for i, comic in enumerate(user["carrinho"], start=1):
                    print(f"[{i}] {comic['nome']}")

                print("\n[1] Remover item")
                print("[0] Voltar ao menu principal")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    item = input("Digite o número do item que deseja remover: ")

                    if item.isdigit() and 1 <= int(item) <= len(user["carrinho"]):
                        removido = user["carrinho"].pop(int(item) - 1)
                        saveFile(dados)
                        print(f"{removido['nome']} removido do carrinho.")

                    else:
                        print("Número inválido.")

                elif opcao != "0":
                    print("Opção inválida.")

            menu_principal(username)
            return


def buyMenu(comic, username):
    print("\n################### COMPRA ###################")
    print(f"Produto: {comic['nome']}")
    print("A funcionalidade de pagamento ainda não foi implementada.")

    menu_principal(username)


def stockCheck():
    showStock()
    menu_admin()


def stockEditing():
    print("\n################### EDIÇÃO DE ESTOQUE ###################")

    dados = openFile()
    estoque = dados["loja_info"]["estoque"]
    
    
    for editora, colecoes in estoque.items():
        print(f"\n################### {editora} ###################")
    
        for nome_saga, quadrinhos in colecoes.items():
            print(f"\n################### {nome_saga} ###################")
    
        for quadrinho in quadrinhos:
            print(f"{quadrinho['nome']} - {quadrinho['autores']}")

        comic = input("Digite o título do quadrinho que deseja editar: ")

        if comicValidation(comic):
            

    menu_admin()


def main():
    try:
        openFile()

    except FileNotFoundError:
        dados = createFile()
        saveFile(dados)

    print("##################### BEM-VINDO AO SISTEMA DE GERENCIAMENTO DA AMALGAMA COMIX! #####################")

    menu_inicial()


main()