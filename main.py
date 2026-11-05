import json

def createFile():
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
                "livro": None,
                "autor": None,
                "data": None
            },
            "carrinho": {
                "usuario": {
                    "livros_selecionados": None
                }
            }
        }
    }

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file)

def openFile():
    with open('data.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

def main():
    if not openFile():
        createFile()
