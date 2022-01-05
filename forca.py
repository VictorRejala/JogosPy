import random

def jogar():

    mensagem_abertura()

    tema = escolha_tema()

    palavra_secreta = carrega_palavra_secreta(tema)

    # Inicializa letras acertadas
    letras_acertadas = ["_" for letra in palavra_secreta]
    confere_espaço(palavra_secreta, letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    print("DICA: Você pode consultar as letras que já falou, basta digitar 1")

    print(letras_acertadas)

    letras_chutadas = []

    while(not acertou and not enforcou):

        chute = pede_chute()

        if(chute == "1"):

            # Mostra as letras ja foram faladas
            print("Essas são as letras que você ja falou: {}".format(letras_chutadas))
            print(letras_acertadas)
            continue

        if(chute == palavra_secreta):

            # Chute completo com o nome certo
            acertou = True
            continue

        else:

            if(chute in letras_chutadas):

                print("Você ja falou essa letra! \nEssas são as letras que você já falou: {}".format(letras_chutadas))

                continue

            else:

                if(chute in palavra_secreta):

                    chute_correto(chute, letras_acertadas, palavra_secreta)

                else:

                    erros += 1

                    desenha_forca(erros)


        letras_chutadas.append(chute)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


    if (acertou):

        mensagem_vencedor()

    else:
        mensagem_perdedor(palavra_secreta)

# Fim do jogo
#------------------------------------------------------------------

# Funções

def escolha_tema():
    opcao_valida = False

    while (not opcao_valida):

        tema = int(input("(1) Frutas (2) Marcas (3) Paises \nQual tema você quer? "))

        if (tema == 1):

            tema = "frutas.txt"
            opcao_valida = True

        elif (tema == 2):

            tema = "marcas.txt"
            opcao_valida = True

        elif (tema == 3):

            tema = "paises.txt"
            opcao_valida = True

        else:

            print("Opção Inválida!!! \nEscolha entre as opções disponíveis!")
            opcao_valida = False

    return tema


def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta(tema):
    arquivo = open(tema, "r", encoding="utf-8")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def pede_chute():
    chute = input("Qual a letra você escolhe? ")
    chute = chute.strip().upper()

    return chute

def confere_espaço(palavra_secreta, letras_acertadas):
    index = 0

    for letra in palavra_secreta:

        if(" " == letra):
            letras_acertadas[index] = letra

        index += 1


def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0

    for letra in palavra_secreta:

        if(chute == letra):
            letras_acertadas[index] = letra

        index += 1


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