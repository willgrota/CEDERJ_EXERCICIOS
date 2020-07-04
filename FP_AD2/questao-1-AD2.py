#SUBPROGRAMAS

def geraPesoLista(list):
    pesoLista = []
    for i in range(len(list)):
        pesoLista.append(float(list[i]))
    return pesoLista

def geraMatrizDados(qtdCand):
    def geraDadosLista(list):
        dadosLista = []
        for i in range(len(list)):
            if i < 1:
                dadosLista.append(str(list[i]))
            elif i == 1:
                dadosLista.append(int(list[i]))
            else:
                dadosLista.append(float(list[i]))
        return dadosLista


    matriz = []
    for i in range(qtdCand):
        dados = input().split()
        matriz.append(geraDadosLista(dados))
    return matriz

def calculaMedia(peso,dados):
    for i in range(len(dados)):
        soma = 0
        l = 0
        for j in range(2,7):
            soma += dados[i][j]*peso[l]
            l += 1
        dados[i].append(soma/10)
    return None


def trocaPos(vals, posX, posY, ind):
    if vals[posY][ind] < vals[posX][ind]:
        temp = vals[posY]
        vals[posY] = vals[posX]
        vals[posX] = temp
    return None

def classificaMedia(dados):
    for tamanho in range(len(dados) - 1, 0, -1):
        for i in range(tamanho):
            if dados[i][7] > dados[i + 1][7]:
                trocaPos(dados, i, i + 1, 7)
    return None


def desempateClassificacao(dados):
    for tamanho in range(len(dados) - 1, 0, -1):
        for i in range(tamanho):
            if dados[i][7] == dados[i + 1][7]:
                if dados[i][1] == dados[i + 1][1]:
                    trocaPos(dados, i + 1, i, 0)
                else:
                    trocaPos(dados, i, i + 1, 1)
    return None

def imprimeClassificacao(dados):
    ind = len(dados)-1
    while ind >= 0:
        print(dados[ind][0])
        ind-=1
    return None


#PROGRAMA PRINCIPAL

peso = input().split()
pesoLista = geraPesoLista(peso)
N = int(input())
matrizDados = geraMatrizDados(N)
calculaMedia(pesoLista,matrizDados)
classificaMedia(matrizDados)
desempateClassificacao(matrizDados)
imprimeClassificacao(matrizDados)




