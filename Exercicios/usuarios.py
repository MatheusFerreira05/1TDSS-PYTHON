usuario = {1:["Matheus","matheus@email.com",123455],2:["Math2","mathzinhi@email.com",16561]}

resp = input("O que você quer fazer? 1-Adicionar um novo usuário 2- Ver usuários cadastrados")

def adiciona():
    id = list(usuario.keys())
    usuario[id[len(id)-1]+1] = [input("Insira um Nome "),input("Insira o Email "),input("Insira um telefone ")]
def relatorio():
    for index,lista in usuario.items():
        print("\n Id: ",index)
        print("Nome: ",lista[0])
        print("Email: ",lista[1])
        print("Telefone: ",lista[2])

if (resp == "1"):
    adiciona()
    resp2 = input("Deseja ver os usuários cadastrados? 1-Sim 2-Não")
    if(resp2 == "1"):
        relatorio()
    else:
        print("Código Finalizado")
elif(resp == "2"):
    relatorio()