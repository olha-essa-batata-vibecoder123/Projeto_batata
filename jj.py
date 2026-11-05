
def funcao():
    try:
        x=int(input("Digite [0, 1 ou 2]: "))
    except:
        print("O valor não é válido")
        return funcao()
    return(x)

print("Seja bem-vindo à AMALGAMA COMIX")
print("-----------MENU-----------")
print("Digite [0] para cadastrar\nDigite [1] para ENTRAR\nDigite [2] para sair\n")
y=funcao()
while y>2 or y<0:
    x=int(input("Digite um número válido: "))
match y:
    case 0:
        print("rodrigo é gay")





