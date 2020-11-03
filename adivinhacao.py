import random


def jogar():
    print("************************************")
    print("Bem vindo ao jogo de Adivinhação...")
    print("************************************")

    def carrega_nivel():
        while True:
            print('Escolha um nível para o jogo.  Fácil (1),  Médio (2), Difícil (3)')
            escolha_dificuldade = int(input('Digite uma das opções: '))

            if escolha_dificuldade == 1:
                print('Você escolheu dificuldade fácil.')
                return 6
            elif escolha_dificuldade == 2:
                print('Você escolheu dificuldade média.')
                return 4
            elif escolha_dificuldade == 3:
                print('Você escolheu dificuldade dificil.')
                return 2
            else:
                print(f'A "{escolha_dificuldade} não é uma opção valida!"')
                continue

    numero_magico = round(random.randrange(1, 101))
    numero_de_chances_restantes = carrega_nivel()

    print(f"Gerei um número aleatório entre 0 ~ 100, você tem {numero_de_chances_restantes + 1} chances.")
    print("Boa Sorte!")
    print("************************************")

    # se palpite for >=10 || <=10 do numero magico : quente
    # se palpite for  >=20 || <=20 do numero magico : morno
    # se palpite for >=30 || <=20 q numero magico : frio
    # se nenhuma das opções, então resposta é igual á: passou longe

    def dica_proximidade_palpite(palpite_jogador):
        proximidade_palpite = abs(numero_magico - palpite_jogador)  # abs - valor absoluto
        exibe_proximidade_palpite(proximidade_palpite)

    def exibe_proximidade_palpite(proximidade_palpite):
        if proximidade_palpite <= 10:
            print("palpite quente")
        elif proximidade_palpite <= 20:
            print("palpite morno")
        elif proximidade_palpite <= 30:
            print("palpite frio")
        else:
            print("passou longe")

    while numero_de_chances_restantes >= 0:
        palpite = int(input("Digite seu palpite: "))

        if palpite < 0 or palpite > 100:
            print('Digite um número entre 0 e 100')
            continue

        dica_proximidade_palpite(palpite)
        acertou = palpite == numero_magico

        if acertou:
            print("Parabéns!!!! você acertou, \"{}\" é o número mágico!!!".format(numero_magico))
            break
        else:
            if numero_de_chances_restantes > 0:
                print("Você ainda tem {} chances.".format(numero_de_chances_restantes), sep=" ")
                numero_de_chances_restantes = numero_de_chances_restantes - 1
            else:
                print("Acabaram todas as suas chances, você perdeu o jogo!")
                print(f"O número mágico era {numero_magico}")
                break


if __name__ == '__main__':
    jogar()
