import adivinhacao
import forca
print('**********Escolha um dos Jogos*********')
print('Jogos: (1) - Adivinhação, (2) Forca')
jogo = int(input("Escolha um dos jogos: "))
if(jogo == 1):
    print('******* Jogando Adivinhação ********')
    adivinhacao.jogar()
elif(jogo == 2):
    print('******* Jogando Forca ********')
    forca.jogar()
