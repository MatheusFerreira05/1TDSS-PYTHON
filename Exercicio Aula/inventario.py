def adicionar(produtos):
    id = list(produtos.keys())
    preco = float(input("Entre com o preço produto: "))
    produtos[id[len(id)-1]+1] = [input("Entre com o nome do produto: ").title(),
    int(input("Entre com o quantidade do produto: ")),
    int(input("Entre com o validade produto: ")),
    int(input("Entre com o lote produto: ")),
    preco,
    input("Entre com a data de entrada do produto: "),
    "",
    preco,
    input("Entre com o nome do departamento: "),
    input("Entre com o nome da filial: ")]
    input("Tecle Enter para continuar")
def relatorio(produtos):
    for index, lista in produtos.items():
       imprimir(index,lista)
       input("Tecle Enter para continuar")
def buscar_simples(produtos):
    busca = int(input("Entre com o ID do produto: "))
    lista = produtos[busca]
    imprimir(busca,lista)
    input("Tecle Enter para continuar")
def buscar(produtos):
    busca = input("Entre com o Nome do produto: ").title()
    for index, lista in produtos.items():
        if busca == lista[0]:
           imprimir(index,lista)
           input("Tecle Enter para continuar")
def alterar(produtos):
    busca = input("Entre com o Nome do produto: ").title()
    for index, lista in produtos.items():
        if busca == lista[0]:
            produtos[index][1] = int(input("Entre com a Nova Quantidade: "))
            imprimir(index,lista)
            input("Tecle Enter para continuar")
def remover(produtos):
    busca = input("Entre com o Nome do produto: ").title()
    for index, lista in produtos.items():
        if busca == lista[0]:
            del produtos[index]
            break
        input("Tecle Enter para continuar")
    relatorio()
def remover_por_index(produtos):
    busca = int(input("Entre com o ID do produto: "))
    del produtos[busca]
    relatorio(produtos)
    input("Tecle Enter para continuar")
def imprimir(index,lista):
    print("\nID:..................", index)
    print("Nome:................", lista[0])
    print("Quantidade:..........", lista[1])
    if lista[2] < 0:
        tempo = "Produto sem validade definida"
    else:
        tempo = str(lista[2])
    print("Validade:............", tempo)
    print("Lote:................", lista[3])
    print("Valor de compra:.....", lista[4])
    print("Data de entrada:.....", lista[5])
    if  lista[6] == "":
        tmp = "Produto não vendido!"
    else:
        tmp = lista[6]
    print("Data de Saida:.......", tmp)
    print("Valor Atualizado:....", lista[7])
    print("Valor total alocado:.", (int(lista[4])*int(lista[1])))
    print("Departamento:........", lista[8])
    print("Filial:..............", lista[9])
