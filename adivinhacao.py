import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tenativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite um numero entre 1 e 100: ")

        chute = int(chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 1000!")
            continue

        print("Você digitou", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
                if (rodada == total_tentativas):
                    pontos = round(pontos / 2)
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif menor:
                print("O seu chute foi menor do que o número secreto!")
                if (rodada == total_tentativas):
                    pontos = round(pontos / 2)
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()