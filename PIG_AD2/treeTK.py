from BalancedBSTSet import *
from tkinter import *



#------------------------------------1) função que recebe array ordenado com todos elementos de uma árvore binária e
#------------------------------------monta o gráfico recursivamente
#------------------------------------2) Não monta o gráfico de acordo com a estrutura real da árvore
#------------------------------------3) Não é usado neste programa, deve permanecer comentado
"""def draw_tree(nodes, pas_vert, pas_horiz,lin,x,y, alt):
    if lin < alt+1:

        if nodes.__len__() % 2 == 0:
            middle = (((nodes.__len__()) // 2) - 1)
        else:
            middle = ((nodes.__len__()) // 2)

        key = nodes[middle]
        x_dir, y_dir = (x + pas_horiz[lin-1]), (y + pas_vert)
        x_esq, y_esq = (x - pas_horiz[lin-1]), (y + pas_vert)
        o = c.create_oval(x-5, y-5, x+5, y+5, outline="blue", width=5, fill="blue")
        t = c.create_text(x+25, y, text = key, font="Arial 10")
        lin += 1

        if middle >= 1:
            l1 = c.create_line(x, y, x_dir, y_dir, fill="black", width=2)
            l2 = c.create_line(x, y, x_esq, y_esq, fill="black", width=2)
            nodes_left = nodes[0: middle]
            nodes_right = nodes[middle + 1: nodes.__len__()]
            draw_tree(nodes_left, pas_vert, pas_horiz,lin,x_esq,y_esq, alt)
            draw_tree(nodes_right, pas_vert, pas_horiz,lin,x_dir,y_dir, alt)
        else:
            if nodes.__len__() > 1:
                l1 = c.create_line(x, y, x_dir, y_dir, fill="black", width=2)
                nodes_right = nodes[1:2]
                draw_tree(nodes_right, pas_vert, pas_horiz,lin,x_dir,y_dir, alt)

    else:
        if lin == alt+1:
            key = nodes[0]
            o = c.create_oval(x - 5, y - 5, x + 5, y + 5, outline="red", width=5, fill="red")
            t = c.create_text(x + 25, y, text=key, font="Arial 10")"""



#----------------------------------------funcao que recebe a raiz da árvore e visita recursivamente
# ---------------------------------------os filhos até as folhas, montando o grafico da árvore
#----------------------------------------usada pela função "graficoArvore"
def draw_tree(node, pas_vert, pas_horiz,lin,x,y, alt,coord):

    if lin < alt + 1:
        key = node.data
        x_dir, y_dir = (x + pas_horiz[lin - 1]), (y + pas_vert)
        x_esq, y_esq = (x - pas_horiz[lin - 1]), (y + pas_vert)
        if node.right == None and node.left == None:
            o = c.create_oval(x - 5, y - 5, x + 5, y + 5, outline="red", width=5, fill="red")
        else:
            o = c.create_oval(x - 5, y - 5, x + 5, y + 5, outline="blue", width=5, fill="blue")
        t = c.create_text(x + 25, y, text=key, font="Arial 10")
        coord.append([x,y,key])
        lin += 1

        if node.right != None:
            l1 = c.create_line(x, y, x_dir, y_dir, fill="black", width=2)
            draw_tree(node.right, pas_vert, pas_horiz, lin, x_dir, y_dir, alt, coord)

        if node.left != None:
            l2 = c.create_line(x, y, x_esq, y_esq, fill="black", width=2)
            draw_tree(node.left, pas_vert, pas_horiz, lin, x_esq, y_esq, alt, coord)

    else:
        if lin == alt + 1:
            key = node.data
            o = c.create_oval(x - 5, y - 5, x + 5, y + 5, outline="red", width=5, fill="red")
            t = c.create_text(x + 25, y, text=key, font="Arial 10")
            coord.append([x, y, key])



#---------------------função que calcula a distribuição dos nós no canvas
#---------------------usada pela função "graficoArvore"
def dimensao(bst):
    a = bst.root()
    alt = bst.height()
    margem_h = 20
    margem_v = 70
    if alt > 0: pas_vert = int((512-margem_v)//alt)
    else: pas_vert = 0
    pas_horiz = [0]*alt
    for i in range(len(pas_horiz)):
        pas_horiz[i] = int((1024-margem_h)//2**(i+2))

    return pas_horiz, pas_vert, alt, a



#-----------------1) funcao que inicia construção do gráfico da árvore
#-----------------2) chama a função que calcula a distribuição dos nós no canvas "dimensao"
#-----------------3) chama a função que desenha os elementos da árvore no canvas "draw_tree", e armazena suas
# ----------------coordenadas no vetor "coord"
def graficoArvore(bst, coord):
    pas_horiz, pas_vert, alt, a = dimensao(bst)
    draw_tree(a, pas_vert, pas_horiz, 1, 512, 30, alt, coord)
    t1 = c.create_text(170, 20, text="1) Clique com botão direiro sobre a tela para OPÇÕES", font="Arial 10")
    t2 = c.create_text(180, 50, text="2) Clique com botão esquerdo sobre um nó para EXCLUIR", font="Arial 10")




#------------------------função que remove nós da árvore com clique do mouse
#------------------------chama a funcão que inicia construção do gráfico da árvore "graficoArvore"
def removeNo(e):

    node = None
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    for i in range(len(coord)):
        if coord[i][0]+5 >= x >= coord[i][0]-5 and coord[i][1]+5 >= y >= coord[i][1]-5:
            node = coord[i][2]

    if node != None:
        bst.remove(int(node))
        c.delete("all")

        graficoArvore(bst,coord)

        print("Nó removido com sucesso: ", node, "\n\n")
        print("Estrutura atualizada da Árvore:\n")
        print("root =", bst.root(), "\n")
        for i in bst:
            print(bst.getcounter(i))
        print("\n\n")

    else: return None



#-----------------------------função que cria a Árvore e adiciona os nós conforme escolhido no menu "opcao"
#-----------------------------traça o gráfico da nova árvore criada
def genBST(arr):
    global bst
    bst = BalancedBSTSet(self_balancing=True)
    for i in arr:
        bst.add (int( i ))
    c.delete("all")
    graficoArvore(bst, coord)
    print("Estrutura da Nova Árvore:\n")
    print("root =", bst.root(), "\n")
    for i in bst:
        print(bst.getcounter(i))
    print("\n\n")
    return


#----------------------------------callback para uma das 3 seleções possíveis do menu "opcao"
#----------------------------------gera uma nova árvore a partir dos nós contidos no arquivo nodes.tx
def genArquivo():
    arr = []
    print("\nÁrvore gerada a partir do arquivo nodes.txt\n")
    try:
        f = open("nodes.txt", 'r')
    except IOError:
        print('TreeTK: Falha ao tentar abir nodes.txt')
        raise
    for line in f:
        arr.append(int(line))
    f.close()
    genBST(arr)


#-------------------------------------callback para uma das 3 seleções possíveis do menu "opcao"
#-------------------------------------gera uma nova árvore aleatoriamente
def genAleatorio():
    print("\nÁrvore gerada aleatoriamente\n")
    arr = generateRandomArray(20, 60)
    print("aleatorio")
    genBST(arr)


#-------------------------------------callback para uma das 3 seleções possíveis do menu "opcao"
#-------------------------------------gera uma nova árvore a partir dos nós fornecidos pelo usuário
def genUsuario():
    print("\nÁrvore gerada a partir dos nós do usuário\n")
    def gerar():
        arr = e.get()
        arr = arr.split()
        genBST(arr)
        entrada.destroy()

    entrada = Tk()
    l = Label(entrada, text="Digite os nós separados por espaço:")
    l.pack()
    e = Entry(entrada, font="Arial 24")
    e.pack()
    i = Button(entrada, text="Gerar", command=gerar)
    i.pack()





#---------------------------------  -criacao dos elementos graficos
arr1 = generateRandomArray(20, 60)
coord = []
master = Tk()
master.geometry("1024x512")
def popup(e): menu.post(e.x_root, e.y_root)
menu = Menu(master, tearoff=0)
menu.add_command(label="Gerar Árvore a partir de nodes.txt", command=genArquivo)
menu.add_command(label="Gerar Árvore randomicamente", command=genAleatorio)
menu.add_command(label="Gerar Árvore com nós digitados", command=genUsuario)
c = Canvas(master, width=1024, height=512)
genBST(arr1)
c.bind("<Button-1>", removeNo)
c.bind("<Button-3>", popup)
c.pack()
mainloop()
