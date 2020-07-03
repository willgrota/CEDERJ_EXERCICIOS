
import struct
TAM = 8

# Subprogramas

def ler(arq):
    inteiro = struct.unpack("=i", arq.read(4))[0]
    flutuante = struct.unpack("=f", arq.read(4))[0]
    return inteiro, flutuante

# Programa Principal

intTest = int(input())
flutTest = float(input())



with open("valores.bin", "r+b") as arq:
    arq.seek(0)
    qtdReg = struct.unpack("=i", arq.read(4))[0]
    chave = 0
    print("ANTES")                         #teste de funcionamento  -  string para titulo
    while chave < qtdReg:
        arq.seek(4+(chave * TAM))
        inteiro, flutuante= ler(arq)

        # teste de funcionamento   lê os valores antes da comparação e de modificação
        print("inteiro:", inteiro, "flutuante:", flutuante)



        if inteiro < intTest and flutuante > flutTest:
            arq.seek(4 + (chave * TAM))
            arq.write(struct.pack("=i", -1))
            arq.write(struct.pack("=f", 9999.0))

        elif inteiro < intTest:
            arq.seek(4 + (chave * TAM))
            arq.write(struct.pack("=i", -1))
            arq.write(struct.pack("=f", flutuante))

        else:
            if flutuante > flutTest:
                arq.seek(4 + (chave * TAM))
                arq.write(struct.pack("=i", inteiro))
                arq.write(struct.pack("=f", 9999.0))
        chave += 1

    #teste de funcionamento     # lê valores após comparação e modificação
    chaveteste = 0
    print("\nAPÓS")
    while chaveteste < qtdReg:
        arq.seek(4 + (chaveteste * TAM))
        inteiro, flutuante = ler(arq)
        print("inteiro:", inteiro, "flutuante:", flutuante)
        chaveteste += 1