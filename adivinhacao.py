import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)

    rodada = 1

    print("Niveis: (1) Fácil, (2) Médio, (3) Difícil")
    nivel = int(input("Defina o seu nível: "))

    if (nivel == 1):

        total_tentativas = 15

    elif (nivel == 2):

        total_tentativas = 10

    elif (nivel == 3):

        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Acerte o número que estou pensando entre 1 e 100: ")
        chute_int = int(chute_str)

        acertou = chute_int == numero_secreto
        chute_maior = chute_int > numero_secreto
        chute_menor = chute_int < numero_secreto

        if (chute_int < 1 or chute_int > 100):

            print("Você deve digitar um número entre 1 e 100")
            print("------------------------------------------")
            continue

        if (acertou):

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
            print("O número pensado realmente era {}!".format(numero_secreto))
            print("---------------------------------")
            break

        else:

            if(chute_maior):

                print("Você errou! O seu chute foi maior que o esperado")

            elif(chute_menor):

                print("Você errou! O seu chute foi menor que o esperado")

        if (rodada == total_tentativas):

            print("Você perdeu! O número pensado era {}".format(numero_secreto))

        print("------------------------------------------------")

if (__name__ == "__main__"):
    jogar()