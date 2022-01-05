import random

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    frutas = ["maça", "banana", "abacate", "acerola", "cereja", "framboesa", "melancia", "pessego", "laranja"]
    marcas = ["calvin-klein"]
    paises = ["brasil", "afeganistao", "alemanha", "bolivia", "bahamas", "canada", "china", "colombia",
              "croacia", "espanha", "hungria", "maldivas", "portugal", "uruguai"]

    opcao_valida = False

    while(not opcao_valida):

        tema = int(input("(1) Frutas (2) Marcas (3) Paises \nQual tema você quer? "))

        if(tema == 1):

            numero_aleatorio = random.randrange(0, len(frutas))
            palavra_secreta = frutas[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        elif(tema == 2):

            numero_aleatorio = random.randrange(0, len(marcas))
            palavra_secreta = marcas[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        elif(tema == 3):

            numero_aleatorio = random.randrange(0, len(paises))
            palavra_secreta = paises[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        else:

            print("Opção Inválida!!! \nEscolha entre as opções disponíveis!")
            opcao_valida = False


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print("A palavra tem ", len(letras_acertadas), "Letras")

    while(not acertou and not enforcou):

        chute = input("\nQual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):

            index = 0

            for letra in palavra_secreta:

                if (chute == letra):
                    letras_acertadas[index] = letra

                index += 1

        else:

            erros += 1

            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):

        mensagem_vencedor()

    else:

        mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    jogar()