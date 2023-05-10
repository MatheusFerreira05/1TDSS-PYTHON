alphabet = ['a','b', 'c', ' ','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listaRotorSimples = ['h',' ', 'o', 'b', 'v', 'q', 'u', 'j', 'f', 'g', 'd', 'n','a', 'i', 'm', 'w', 'c', 'x', 'e', 'k', 'p', 'z', 'r', 'l', 'y', 's', 't']
listaRefletor = ['d',' ','n','h','g','s','f', 'z', 'p', 't', 'y', 'u',
                 'x', 'j', 'k', 'l', 'b', 'o', 'c', 'r', 'q', 'v', 'i', 'e', 'w', 'm', 'a']

mensagem = "testa mensagem top"

for letra in mensagem:
    posicao = alphabet.index(letra)+1
    letras = alphabet[posicao]
    posicaoRotor = listaRotorSimples.index(letras)
    letraRotor = listaRotorSimples[posicaoRotor]
    posicaoRefletor = listaRefletor.index(letraRotor)
    letraRefletor = listaRefletor[posicaoRefletor]
    posicaoAlfa = alphabet.index(letraRefletor)
    letraAlfa = alphabet[posicaoAlfa]
    #print(f"Palavra cifrada: {letraAlfa}")
    
    for letra in letraAlfa:
        posicaoAlfa = alphabet.index(letra)
        letraAlfa = alphabet[posicaoAlfa]
        posicaoRefletor = listaRefletor.index(letraAlfa)
        letraRefletor = listaRefletor[posicaoRefletor]
        posicaoRotor = listaRotorSimples.index(letraRefletor)
        letraRotor = listaRotorSimples[posicaoRotor]
        posicaoAlfa = alphabet.index(letraRotor)-1
        letraAlfa = alphabet[posicaoAlfa]
        msgDecifrada = letraAlfa
    print(f"Palavra decifrada: {msgDecifrada}")
        


    
    