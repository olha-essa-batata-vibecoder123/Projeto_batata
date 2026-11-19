import json
import unicodedata
import os
import sys
import ctypes
import hashlib
import hmac
import secrets
import base64
from getpass import getpass
from difflib import SequenceMatcher


ITERACOES_PBKDF2 = 600_000


def criarHashSenha(senha):
    salt = secrets.token_bytes(16)
    hash_senha = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        ITERACOES_PBKDF2
    )

    return (
        f"pbkdf2_sha256${ITERACOES_PBKDF2}$"
        f"{base64.b64encode(salt).decode('ascii')}$"
        f"{base64.b64encode(hash_senha).decode('ascii')}"
    )


def verificarSenha(senha, senha_armazenada):
    if senha_armazenada.startswith("pbkdf2_sha256$"):
        try:
            algoritmo, iteracoes, salt_b64, hash_b64 = senha_armazenada.split("$")
            salt = base64.b64decode(salt_b64)
            hash_original = base64.b64decode(hash_b64)

            hash_teste = hashlib.pbkdf2_hmac(
                "sha256",
                senha.encode("utf-8"),
                salt,
                int(iteracoes)
            )

            return hmac.compare_digest(hash_teste, hash_original)

        except (ValueError, TypeError):
            return False

    return hmac.compare_digest(senha, senha_armazenada)


def validarSenhaNova(senha):
    if len(senha) < 12:
        print("A senha deve ter pelo menos 12 caracteres.")
        return False

    if not any(c.islower() for c in senha):
        print("A senha precisa ter uma letra minuscula.")
        return False

    if not any(c.isupper() for c in senha):
        print("A senha precisa ter uma letra maiuscula.")
        return False

    if not any(c.isdigit() for c in senha):
        print("A senha precisa ter um numero.")
        return False

    return True


class DATA_BLOB(ctypes.Structure):
    _fields_ = [
        ("cbData", ctypes.c_uint32),
        ("pbData", ctypes.POINTER(ctypes.c_ubyte))
    ]


def _blob(dados):
    buffer = ctypes.create_string_buffer(dados)
    return DATA_BLOB(
        len(dados),
        ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ubyte))
    ), buffer


def criptografarArquivo(conteudo):
    if os.name != "nt":
        raise RuntimeError(
            "A criptografia sem bibliotecas externas desta versao "
            "usa o Windows DPAPI. Execute no Windows."
        )

    entrada, buffer_entrada = _blob(conteudo)
    saida = DATA_BLOB()

    sucesso = ctypes.windll.crypt32.CryptProtectData(
        ctypes.byref(entrada),
        "Amalgama Comix",
        None,
        None,
        None,
        0,
        ctypes.byref(saida)
    )

    if not sucesso:
        raise ctypes.WinError()

    try:
        return ctypes.string_at(saida.pbData, saida.cbData)
    finally:
        ctypes.windll.kernel32.LocalFree(
            ctypes.cast(saida.pbData, ctypes.c_void_p)
        )


def descriptografarArquivo(conteudo):
    if os.name != "nt":
        raise RuntimeError(
            "A criptografia sem bibliotecas externas desta versao "
            "usa o Windows DPAPI. Execute no Windows."
        )

    entrada, buffer_entrada = _blob(conteudo)
    saida = DATA_BLOB()

    sucesso = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(entrada),
        None,
        None,
        None,
        None,
        0,
        ctypes.byref(saida)
    )

    if not sucesso:
        raise RuntimeError(
            "Nao foi possivel descriptografar dados.json. "
            "Use a mesma conta do Windows que criptografou o arquivo."
        )

    try:
        return ctypes.string_at(saida.pbData, saida.cbData)
    finally:
        ctypes.windll.kernel32.LocalFree(
            ctypes.cast(saida.pbData, ctypes.c_void_p)
        )


def _solicitarSenhaAdmin():
    print("\nConfiguracao inicial do administrador.")
    print("Crie uma senha forte com pelo menos 12 caracteres.")

    while True:
        senha = getpass("Nova senha do administrador: ")
        if not validarSenhaNova(senha):
            continue

        confirmacao = getpass("Confirme a senha: ")
        if senha != confirmacao:
            print("As senhas nao coincidem.")
            continue

        return senha


def createFile():
    dados = {
        "user_info": [],

        "user_info_admin": {
            "username": "administrador",
            "senha": criarHashSenha(_solicitarSenhaAdmin())
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
                            "data": "1985–1986",
                            "precos": None
                        }
                        for i in range(1, 13)
                    ]
                }
            }
        }
    }

    return dados


def saveFile(dados):
    conteudo = json.dumps(
        dados,
        ensure_ascii=False,
        indent=4
    ).encode("utf-8")

    conteudo_criptografado = criptografarArquivo(conteudo)

    arquivo_temporario = "dados.tmp"

    with open(arquivo_temporario, "wb") as arquivo:
        arquivo.write(b"AMALGAMA_ENCRYPTED_V1\n")
        arquivo.write(conteudo_criptografado)

    os.replace(arquivo_temporario, "dados.json")


def openFile():
    with open("dados.json", "rb") as arquivo:
        conteudo = arquivo.read()

    marcador = b"AMALGAMA_ENCRYPTED_V1\n"

    if conteudo.startswith(marcador):
        conteudo_criptografado = conteudo[len(marcador):]
        conteudo_json = descriptografarArquivo(conteudo_criptografado)
        return json.loads(conteudo_json.decode("utf-8"))

    dados = json.loads(conteudo.decode("utf-8"))
    saveFile(dados)

    return dados


def normalizarTexto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def buscarObras(termo):
    dados = openFile()
    estoque = dados["loja_info"]["estoque"]

    termo_normalizado = normalizarTexto(termo)
    resultados = []

    for editora, colecoes in estoque.items():
        for saga, quadrinhos in colecoes.items():
            for quadrinho in quadrinhos:

                campos = [
                    quadrinho.get("nome", ""),
                    quadrinho.get("nome_alt", ""),
                    quadrinho.get("autores", ""),
                    quadrinho.get("desenhistas", ""),
                    saga
                ]

                melhor_pontuacao = 0

                for campo in campos:
                    campo_normalizado = normalizarTexto(campo)

                    if termo_normalizado in campo_normalizado:
                        melhor_pontuacao = 1
                        break

                    pontuacao = SequenceMatcher(
                        None,
                        termo_normalizado,
                        campo_normalizado
                    ).ratio()

                    melhor_pontuacao = max(
                        melhor_pontuacao,
                        pontuacao
                    )

                if melhor_pontuacao >= 0.55:
                    resultados.append({
                        "editora": editora,
                        "saga": saga,
                        "quadrinho": quadrinho,
                        "pontuacao": melhor_pontuacao
                    })

    resultados.sort(
        key=lambda resultado: resultado["pontuacao"],
        reverse=True
    )

    return resultados


def signUp():
    print("\nCadastro de usuario")

    nome = input("Digite seu nome: ").strip()
    username = input("Crie um nome de usuario: ").strip()

    if not nome or not username:
        print("Nome e usuario nao podem ficar vazios.")
        menu_inicial()
        return

    senha = getpass("Crie uma senha: ")

    if not validarSenhaNova(senha):
        menu_inicial()
        return

    confirmacao = getpass("Confirme sua senha: ")

    if senha != confirmacao:
        print("As senhas nao coincidem.")
        menu_inicial()
        return

    dados = openFile()

    if username == dados["user_info_admin"]["username"]:
        print("Nome de usuario indisponivel.")
        menu_inicial()
        return

    for user in dados["user_info"]:
        if username == user["username"]:
            print("Nome de usuario ja cadastrado.")
            menu_inicial()
            return

    new_user = {
        "nome": nome,
        "username": username,
        "senha": criarHashSenha(senha),
        "carrinho": []
    }

    dados["user_info"].append(new_user)
    saveFile(dados)

    print(f"Cadastro realizado com sucesso!\nBem-vindo(a), {nome}!")
    menu_principal(username)


def logIn():
    print("Login de usuario")

    username = input("Digite seu nome de usuario: ").strip()
    senha = getpass("Digite sua senha: ")

    dados = openFile()

    admin = dados["user_info_admin"]

    if username == admin["username"]:
        senha_correta = verificarSenha(senha, admin["senha"])

        if senha_correta:
            if not admin["senha"].startswith("pbkdf2_sha256$"):
                admin["senha"] = criarHashSenha(senha)
                saveFile(dados)

            print("Bem-vindo ao menu de administrador!")
            menu_admin()
            return

    for user in dados["user_info"]:
        if username == user["username"]:
            senha_correta = verificarSenha(senha, user["senha"])

            if senha_correta:
                if not user["senha"].startswith("pbkdf2_sha256$"):
                    user["senha"] = criarHashSenha(senha)
                    saveFile(dados)

                print(
                    f"Login realizado com sucesso!\n"
                    f"Bem-vindo(a), {user['nome']}!"
                )
                menu_principal(username)
                return

            break

    print("Nome de usuario ou senha incorretos.")
    menu_inicial()


def menu_inicial():
    print("\n---------- Menu inicial ----------")
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

    comic = normalizarTexto(comic)

    for editora, colecoes in estoque.items():
        for nome_colecao, quadrinhos in colecoes.items():
            for quadrinho in quadrinhos:

                nome_original = normalizarTexto(quadrinho["nome"])
                nome_alternativo = normalizarTexto(
                    quadrinho.get("nome_alt", "")
                )

                if comic == nome_original or comic == nome_alternativo:
                    return quadrinho

    return None


def searchSys(username):
    print("\n########## SISTEMA DE BUSCA ##########")

    print("Digite parte do nome, autor, desenhista ou saga.")
    print("Digite 0 para voltar ao menu.")

    termo = input("\nO que deseja pesquisar? ")

    if termo == "0":
        menu_principal(username)
        return

    resultados = buscarObras(termo)

    if not resultados:
        print("\nNenhuma obra encontrada.")

    else:
        print(f"\nForam encontradas {len(resultados)} obras:")

        for i, resultado in enumerate(resultados, start=1):
            comic = resultado["quadrinho"]

            print(f"\n[{i}] {comic['nome']}")
            print(f"    Nome alternativo: {comic.get('nome_alt', 'Não informado')}")
            print(f"    Editora: {resultado['editora']}")
            print(f"    Saga: {resultado['saga']}")
            print(f"    Autor: {comic['autores']}")

        escolha = input(
            "\nDigite o número da obra para ver detalhes "
            "ou 0 para voltar: "
        )

        if escolha.isdigit():
            numero = int(escolha)

            if 1 <= numero <= len(resultados):
                comic = resultados[numero - 1]["quadrinho"]
                showComicDetails(comic, username)
                return

            elif numero != 0:
                print("Opção inválida.")

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
        print("Obra encontrada.")

    else:
        print("Obra não encontrada.")

    menu_admin()


def main():
    try:
        openFile()

    except FileNotFoundError:
        dados = createFile()
        saveFile(dados)

    print("==================== Bem-vindo à ALMAGAMA COMIX! ====================")

    menu_inicial()


main()