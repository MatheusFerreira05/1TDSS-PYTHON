id = [1, 3]
produtos = ["Banana", "Notebook"]
qtd = [20, 2]
validade = [3, -1]
lote = [12345, 54321]
valor_compra = [1.0, 3500.0]
data_entrada = ["18/03/2023", "01/01/2023"]
data_saida = ["", ""]
valor_atual = [1, 3000]
departamento = ["Copa", "RH"]
filial = ["São Paulo", "São Paulo"]

def adicionar():
    id.append(id[len(id)-1]+1)
    produtos.append(input("Entre com o nome do produto: ").title())
    qtd.append(int(input("Entre com o quantidade do produto: ")))
    validade.append(int(input("Entre com o validade produto: ")))
    lote.append(int(input("Entre com o lote produto: ")))
    preco = float(input("Entre com o preço produto: "))
    valor_compra.append(preco)
    data_entrada.append(input("Entre com a data de entrada do produto: "))
    data_saida.append("")
    valor_atual.append(preco)
    departamento.append(input("Entre com o nome do departamento: "))
    filial.append(input("Entre com o nome da filial: "))

def relatorio():
    for index in range(0, len(id)):
        print("\nID:..................", id[index])
        print("Nome:................", produtos[index])
        print("Quantidade:..........", qtd[index])
        if validade[index] < 0:
            tempo = "Produto sem validade definida"
        else:
            tempo = str(validade[index])
        print("Validade:............", tempo)
        print("Lote:................", lote[index])
        print("Valor de compra:.....", valor_compra[index])
        print("Data de entrada:.....", data_entrada[index])
        if data_saida[index] == "":
            tmp = "Produto não vendido!"
        else:
            tmp = data_saida[index]
        print("Data de Saida:.......", tmp)
        print("Valor Atualizado:....", valor_atual[index])
        print("Valor total alocado:.", (int(valor_compra[index])*int(qtd[index])))
        print("Departamento:........", departamento[index])
        print("Filial:..............", filial[index])

def busca():
    busca = input("Entre com o nome do produto: ").title()
    if busca in produtos:
        for index in range(0, len(id)):
            if busca == produtos[index]:
                print("\nID:..................", id[index])
                print("Nome:................", produtos[index])
                print("Quantidade:..........", qtd[index])
                if validade[index] < 0:
                    tempo = "Produto sem validade definida"
                else:
                    tempo = str(validade[index])
                print("Validade:............", tempo)
                print("Lote:................", lote[index])
                print("Valor de compra:.....", valor_compra[index])
                print("Data de entrada:.....", data_entrada[index])
                if data_saida[index] == "":
                    tmp = "Produto não vendido!"
                else:
                    tmp = data_saida[index]
                print("Data de Saida:.......", tmp)
                print("Valor Atualizado:....", valor_atual[index])
                print("Valor total alocado:.", (int(valor_compra[index])*int(qtd[index])))
                print("Departamento:........", departamento[index])
                print("Filial:..............", filial[index])
    else:
        print("Produto fora de estoque!")

def alterar_preco():
    altera = input("Entre com o nome do produto: ").title()
    if altera in produtos:
        for index in range(0, len(id)):
            if altera == produtos[index]:
                new_preco = float(input("Entre com o novo preço: "))
                valor_atual[index] = new_preco
                print("\nID:..................", id[index])
                print("Nome:................", produtos[index])
                print("Quantidade:..........", qtd[index])
                if validade[index] < 0:
                    tempo = "Produto sem validade definida"
                else:
                    tempo = str(validade[index])
                print("Validade:............", tempo)
                print("Lote:................", lote[index])
                print("Valor de compra:.....", valor_compra[index])
                print("Data de entrada:.....", data_entrada[index])
                if data_saida[index] == "":
                    tmp = "Produto não vendido!"
                else:
                    tmp = data_saida[index]
                print("Data de Saida:.......", tmp)
                print("Valor Atualizado:....", valor_atual[index])
                print("Valor total alocado:.", (int(valor_compra[index])*int(qtd[index])))
                print("Departamento:........", departamento[index])
                print("Filial:..............", filial[index])
    else:
        print("Produto fora de estoque!")

def remover():
    produtos.remove(input("entre com o produto a remover: "))
    #del produtos[0]

def vender():
    ...