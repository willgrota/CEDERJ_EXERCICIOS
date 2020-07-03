

#SUBPROGRAMAS

def corrigePalavra(palavra):
    novaPalavra = palavra
    if len(palavra) > 1:
        if palavra[len(palavra)-1] == palavra[len(palavra)-2]:
            novaPalavra = palavra[0:len(palavra)-1]
        else:
            ind = len(palavra)-3
            ind2 = len(palavra)-2
            while ind > -1:
                if palavra[len(palavra)-1] != palavra[ind]:
                    ind -= 1
                else:
                    ref = ind
                    ind -= 1
                    if palavra[ind2] == palavra[ind]:
                        while palavra[ind2] == palavra[ind] and ind > -1 and ind2 > ref+1:
                            ind -= 1
                            ind2 -= 1
                        novaPalavra = palavra[0:ind2]
    return novaPalavra

def corrigeMensagens(list):
    msgCorrigida = ""
    for i in range(len(list)):
        linha = (str(list[i])).split()
        lnCorrigida = ""
        numCorrigida = 0
        for j in range(len(linha)):
            plv = str(linha[j])
            plCorrigida = corrigePalavra(plv)
            if plv != plCorrigida:
                numCorrigida += 1
            lnCorrigida += plCorrigida + " "
        msgCorrigida += str(numCorrigida) + " " + lnCorrigida.strip() + ", "
    msgCorrigida = msgCorrigida[0:len(msgCorrigida)-2]
    msgCorFinal = msgCorrigida.split(", ")
    return msgCorFinal

def lerArquivoEntrada():
    leitura = open("mensagens_originais.txt", "r")
    N = leitura.readline()
    dados = []
    linha = 1
    msg = ""
    while linha <= int(N):
        if linha < int(N):
            msg = leitura.readline()
            dados.append(msg[0:len(msg) - 1])
            linha += 1
        elif linha == int(N):
            msg = leitura.readline()
            dados.append(msg[0:len(msg)])
            linha += 1
    leitura.close()
    return dados


def escreverArqSaida(dados):
    escrita = open("mensagens_corrigidas.txt", "w")
    for i in range(len(dados)):
        escrita.write(dados[i] + "\n")
    escrita.close()
    print('novo teste')
    return None


#PROGRAMA PRINCIPAL

dadosEnt = lerArquivoEntrada()
msgCorreta = corrigeMensagens(dadosEnt)
dadosSaida = escreverArqSaida(msgCorreta)


