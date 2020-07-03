#SUBPROGRAMAS

def criarConjunto():
    leitura = open("palavras.txt", "r")
    conjunto = set()
    item = leitura.readline()
    while item != "":
        conjunto.add(item.replace("\n",""))
        item = leitura.readline()
    leitura.close()
    return conjunto

def criarString():
    leitura = open("discurso.txt", "r")
    frase = ""
    item = leitura.readline()
    while item != "":
        frase += item.replace("\n"," ")
        item = leitura.readline()
    leitura.close()
    frase = frase.replace("- ", "")
    return frase

def criarDicionario(conjunto, frase):
    fraseList = frase.split()
    verbete = dict()
    for item in conjunto:
        verbete[item] = 0

    for item in conjunto:
        for i in range(len(fraseList)):
            if item == fraseList[i]:
                verbete[item] += 1
    return verbete

def escreverArqSaida(verbete):
    escrita = open("contagem.txt", "w")
    for chave in verbete:
        escrita.write(chave + " ")
        escrita.write(str(verbete[chave]) + "\n")
    escrita.close()
    return None


#PROGRAMA PRINCIPAL

palavras = criarConjunto()
discurso = criarString()
dicionario = criarDicionario(palavras, discurso)
escreverArqSaida(dicionario)

