alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listaRotorSimples = ['h','o','b','v','q','u','j','f','g','d','n','a','i','m','w','c','x','e','k','p','z','r','l','y','s','t']
listaRefletor = ['d','n','h','g','s','f','z','p','t','y','u','x','j','k','l','b','o','c','r','q','v','i','e','w','m','a']

mensagem = "matheus"

for letra in mensagem:
    posicao = alphabet.index(letra)+1
    posicaoRotor = listaRotorSimples[posicao]
    posicaoRefletor = listaRefletor.index(posicaoRotor)
    mensagem = posicaoRefletor
    print(mensagem)
    