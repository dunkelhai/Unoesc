import random

def comojogarf():
    print("\nPara jogar, basta mover sua peça para um espaço vazio e tentar encurralar o outro jogador.\nSempre lembrando que, a cada movimento, precisa prestar"
        "atenção se o movimento que for fazer, não vai deixar uma brecha para seu oponente encurralá-lo.")

def inicijogof():
    print(''' 
 _________________________________
< Pong Hau Ki by Alysson Oliveira >
 ---------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\\
                ||----w |
                ||     ||''')

    print("\nSeja Bem-vindo ao Pong Hau Ki!\n\nEsse jogo, é um jogo de tabuleiro Chinês, que tem como objetivo, impedir com que seu oponente possa mover suas peças."
      "\n\nDeseja saber como jogar?")

inicijogof()

comojogar = input("1- Para SIM\n2- Para Não\n")
if comojogar == "1":
    comojogarf()
    tipojogar = input(
        "\nDeseja jogar contra a Máquina ou contra outro Jogador local?\n\n1- Para Máquina \n2- Para Jogador\n")
else:
    tipojogar = input("\nDeseja jogar contra a Máquina ou contra outro Jogador local?\n\n1- Para Máquina \n2- Para Jogador\n")

posicoes = [1, 3, 0, 2, 4]

def tabuleiro():
    tabuleiroJogada = ("[" + str(posicoes[0]) + "]\     /[" + str(posicoes[1]) + "]\n |   [" + str(posicoes[2]) + "]   | \n[" + str(posicoes[3]) + "]/-----\[" + str(posicoes[4]) + "]")
    print(tabuleiroJogada)

def vitoriajogadorvsjogador():
    if posicoes[0] == 0 and posicoes[2] == 1 and posicoes[3] == 3:
        print("\nJogador 1 Venceu!")
        return True
    elif posicoes[0] == 0 and posicoes[2] == 3 and posicoes[3] == 1:
        print("\nJogador 1 Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 1 and posicoes[4] == 3:
        print("\nJogador 1 Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 3 and posicoes[4] == 1:
        print("\nJogador 1 Venceu!")
        return True
    if posicoes[0] == 0 and posicoes[2] == 2 and posicoes[3] == 4:
        print("\nJogador 2 Venceu!")
        return True
    elif posicoes[0] == 0 and posicoes[2] == 4 and posicoes[3] == 2:
        print("\nJogador 2 Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 2 and posicoes[4] == 4:
        print("\nJogador 2 Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 4 and posicoes[4] == 2:
        print("\nJogador 2 Venceu!")
        return True

def vitoriajogadorvsmaquina():
    if posicoes[0] == 0 and posicoes[2] == 1 and posicoes[3] == 3:
        print("\nJogador 1 Venceu!")
        return True
    elif posicoes[0] == 0 and posicoes[2] == 3 and posicoes[3] == 1:
        print("\nJogador 1 Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 1 and posicoes[4] == 3:
        print("\nJogador 1 Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 3 and posicoes[4] == 1:
        print("\nJogador 1 Venceu!")
        return True
    if posicoes[0] == 0 and posicoes[2] == 2 and posicoes[3] == 4:
        print("\nMáquina Venceu!")
        return True
    elif posicoes[0] == 0 and posicoes[2] == 4 and posicoes[3] == 2:
        print("\nMáquina Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 2 and posicoes[4] == 4:
        print("\nMáquina Venceu!")
        return True
    elif posicoes[1] == 0 and posicoes[2] == 4 and posicoes[4] == 2:
        print("\nMáquina Venceu!")
        return True

def jogadorvsjogador():
    turno = 1
    while not vitoriajogadorvsjogador():
        if turno % 2 != 0:
            if vitoriajogadorvsjogador():
                break
            else:
                movimentoj1 = input("\nSua vez Jogador 1.\nPor favor, escolha de acordo com mapa das posições mostrado no começo, uma posição que contenha sua peça para movimentá-la para um espaço válido:\n")

            if movimentoj1 == "1":
                if posicoes.index(0) == 2 and posicoes.index(1) == 0 and movimentoj1 == "1":
                    posicoes[0] = 0
                    posicoes[2] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 2 and posicoes.index(0) == 0 and movimentoj1 == "1":
                    posicoes[0] = 1
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 3 and posicoes.index(0) == 2 and movimentoj1 == "1":
                    posicoes[3] = 0
                    posicoes[2] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(1) == 2 and movimentoj1 == "1":
                    posicoes[3] = 1
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 3 and posicoes.index(0) == 0 and movimentoj1 == "1":
                    posicoes[3] = 0
                    posicoes[0] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(1) == 0 and movimentoj1 == "1":
                    posicoes[3] = 1
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 3 and posicoes.index(0) == 4 and movimentoj1 == "1":
                    posicoes[3] = 0
                    posicoes[4] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(1) == 4 and movimentoj1 == "1":
                    posicoes[3] = 1
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 1 and posicoes.index(0) == 2 and movimentoj1 == "1":
                    posicoes[2] = 1
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(1) == 2 and movimentoj1 == "1":
                    posicoes[2] = 0
                    posicoes[1] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 2 and posicoes.index(0) == 4 and movimentoj1 == "1":
                    posicoes[2] = 0
                    posicoes[4] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 2 and posicoes.index(1) == 4 and movimentoj1 == "1":
                    posicoes[2] = 1
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 1 and posicoes.index(0) == 4 and movimentoj1 == "1":
                    posicoes[1] = 0
                    posicoes[4] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(1) == 4 and movimentoj1 == "1":
                    posicoes[1] = 1
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"

                # Aqui tem treta kkkk

                # Avalia posição do 1 na 0
                if posicoes.index(1) == 0 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(
                        3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 0 and (posicoes.index(2) == 3 and movimentoj1 == "1" or posicoes.index(
                        3) == 3 and movimentoj1 == "1" or posicoes.index(4) == 3 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 1 na 3
                if posicoes.index(1) == 3 and (posicoes.index(2) == 4 and movimentoj1 == "1" or posicoes.index(
                        3) == 4 and movimentoj1 == "1" or posicoes.index(4) == 4 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 3 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(
                        3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 3 and (posicoes.index(2) == 0 and movimentoj1 == "1" or posicoes.index(
                        3) == 0 and movimentoj1 == "1" or posicoes.index(4) == 0 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 1 na 2
                if posicoes.index(1) == 2 and (posicoes.index(2) == 4 and movimentoj1 == "1" or posicoes.index(
                        3) == 4 and movimentoj1 == "1" or posicoes.index(4) == 4 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 2 and (posicoes.index(2) == 1 and movimentoj1 == "1" or posicoes.index(
                        3) == 1 and movimentoj1 == "1" or posicoes.index(4) == 1 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 2 and (posicoes.index(2) == 3 and movimentoj1 == "1" or posicoes.index(
                        3) == 3 and movimentoj1 == "1" or posicoes.index(4) == 3 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 2 and (posicoes.index(2) == 0 and movimentoj1 == "1" or posicoes.index(
                        3) == 0 and movimentoj1 == "1" or posicoes.index(4) == 0 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 1 na 1
                if posicoes.index(1) == 1 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(
                        3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 1 and (posicoes.index(2) == 4 and movimentoj1 == "1" or posicoes.index(
                        3) == 4 and movimentoj1 == "1" or posicoes.index(4) == 4 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 1 na 4
                if posicoes.index(1) == 4 and (posicoes.index(2) == 3 and movimentoj1 == "1" or posicoes.index(
                        3) == 3 and movimentoj1 == "1" or posicoes.index(4) == 3 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 4 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(
                        3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 4 and (posicoes.index(2) == 1 and movimentoj1 == "1" or posicoes.index(
                        3) == 1 and movimentoj1 == "1" or posicoes.index(4) == 1 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

            elif movimentoj1 == "3":
                if posicoes.index(0) == 2 and posicoes.index(3) == 0 and movimentoj1 == "3":
                    posicoes[0] = 0
                    posicoes[2] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 2 and posicoes.index(0) == 0 and movimentoj1 == "3":
                    posicoes[0] = 3
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 3 and posicoes.index(0) == 2 and movimentoj1 == "3":
                    posicoes[3] = 0
                    posicoes[2] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(3) == 2 and movimentoj1 == "3":
                    posicoes[3] = 3
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 3 and posicoes.index(0) == 0 and movimentoj1 == "3":
                    posicoes[3] = 0
                    posicoes[0] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(3) == 0 and movimentoj1 == "3":
                    posicoes[3] = 3
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 3 and posicoes.index(0) == 4 and movimentoj1 == "3":
                    posicoes[3] = 0
                    posicoes[4] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(3) == 4 and movimentoj1 == "3":
                    posicoes[3] = 3
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 1 and posicoes.index(0) == 2 and movimentoj1 == "3":
                    posicoes[2] = 3
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(3) == 2 and movimentoj1 == "3":
                    posicoes[2] = 0
                    posicoes[1] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 2 and posicoes.index(0) == 4 and movimentoj1 == "3":
                    posicoes[2] = 0
                    posicoes[4] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 2 and posicoes.index(3) == 4 and movimentoj1 == "3":
                    posicoes[2] = 3
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 1 and posicoes.index(0) == 4 and movimentoj1 == "3":
                    posicoes[1] = 0
                    posicoes[4] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(3) == 4 and movimentoj1 == "3":
                    posicoes[1] = 3
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"

                # Avalia posição do 3 na 0
                if posicoes.index(3) == 0 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 0 and (posicoes.index(2) == 3 and movimentoj1 == "3" or posicoes.index(1) == 3 and movimentoj1 == "3" or posicoes.index(4) == 3 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 3
                if posicoes.index(3) == 3 and (posicoes.index(2) == 4 and movimentoj1 == "3" or posicoes.index(1) == 4 and movimentoj1 == "3" or posicoes.index(4) == 4 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 3 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 3 and (posicoes.index(2) == 0 and movimentoj1 == "3" or posicoes.index(1) == 0 and movimentoj1 == "3" or posicoes.index(4) == 0 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 2
                if posicoes.index(3) == 2 and (posicoes.index(2) == 4 and movimentoj1 == "3" or posicoes.index(1) == 4 and movimentoj1 == "3" or posicoes.index(4) == 4 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 2 and (posicoes.index(2) == 1 and movimentoj1 == "3" or posicoes.index(1) == 1 and movimentoj1 == "3" or posicoes.index(4) == 1 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 2 and (posicoes.index(2) == 3 and movimentoj1 == "3" or posicoes.index(1) == 3 and movimentoj1 == "3" or posicoes.index(4) == 3 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 2 and (posicoes.index(2) == 0 and movimentoj1 == "3" or posicoes.index(1) == 0 and movimentoj1 == "3" or posicoes.index(4) == 0 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 1
                if posicoes.index(3) == 1 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 1 and (posicoes.index(2) == 4 and movimentoj1 == "3" or posicoes.index(1) == 4 and movimentoj1 == "3" or posicoes.index(4) == 4 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 4
                if posicoes.index(3) == 4 and (posicoes.index(2) == 3 and movimentoj1 == "3" or posicoes.index(1) == 3 and movimentoj1 == "3" or posicoes.index(4) == 3 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 4 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 4 and (posicoes.index(2) == 1 and movimentoj1 == "3" or posicoes.index(1) == 1 and movimentoj1 == "3" or posicoes.index(4) == 1 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")

            else:
                print("\nPor favor, faça um movimento válido! Selecione um número ímpar disponível para movimentar 1 ou 3.")

        if turno % 2 == 0:
            if vitoriajogadorvsjogador():
                break
            else:
                movimentoj2 = input("\nSua vez Jogador 2.\nPor favor, escolha de acordo com mapa das posições mostrado no começo, uma posição que contenha sua peça para movimentá-la para um espaço válido:\n")

            if movimentoj2 == "2":
                if posicoes.index(0) == 2 and posicoes.index(2) == 0 and movimentoj2 == "2":
                    posicoes[0] = 0
                    posicoes[2] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 2 and posicoes.index(0) == 0 and movimentoj2 == "2":
                    posicoes[0] = 2
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 3 and posicoes.index(0) == 2 and movimentoj2 == "2":
                    posicoes[3] = 0
                    posicoes[2] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(2) == 2 and movimentoj2 == "2":
                    posicoes[3] = 2
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 3 and posicoes.index(0) == 0 and movimentoj2 == "2":
                    posicoes[3] = 0
                    posicoes[0] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(2) == 0 and movimentoj2 == "2":
                    posicoes[3] = 2
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 3 and posicoes.index(0) == 4 and movimentoj2 == "2":
                    posicoes[3] = 0
                    posicoes[4] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(2) == 4 and movimentoj2 == "2":
                    posicoes[3] = 2
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 1 and posicoes.index(0) == 2 and movimentoj2 == "2":
                    posicoes[2] = 2
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(2) == 2 and movimentoj2 == "2":
                    posicoes[2] = 0
                    posicoes[1] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 2 and posicoes.index(0) == 4 and movimentoj2 == "2":
                    posicoes[2] = 0
                    posicoes[4] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 2 and posicoes.index(2) == 4 and movimentoj2 == "2":
                    posicoes[2] = 2
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 1 and posicoes.index(0) == 4 and movimentoj2 == "2":
                    posicoes[1] = 0
                    posicoes[4] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(2) == 4 and movimentoj2 == "2":
                    posicoes[1] = 2
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"

                # Avalia posição do 2 na 0
                if posicoes.index(2) == 0 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 0 and (posicoes.index(3) == 3 and movimentoj2 == "2" or posicoes.index(1) == 3 and movimentoj2 == "2" or posicoes.index(4) == 3 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 3
                if posicoes.index(2) == 3 and (posicoes.index(3) == 4 and movimentoj2 == "2" or posicoes.index(1) == 4 and movimentoj2 == "2" or posicoes.index(4) == 4 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 3 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 3 and (posicoes.index(3) == 0 and movimentoj2 == "2" or posicoes.index(1) == 0 and movimentoj2 == "2" or posicoes.index(4) == 0 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 2
                if posicoes.index(2) == 2 and (posicoes.index(3) == 4 and movimentoj2 == "2" or posicoes.index(1) == 4 and movimentoj2 == "2" or posicoes.index(4) == 4 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 2 and (posicoes.index(3) == 1 and movimentoj2 == "2" or posicoes.index(1) == 1 and movimentoj2 == "2" or posicoes.index(4) == 1 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 2 and (posicoes.index(3) == 3 and movimentoj2 == "2" or posicoes.index(1) == 3 and movimentoj2 == "2" or posicoes.index(4) == 3 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 2 and (posicoes.index(3) == 0 and movimentoj2 == "2" or posicoes.index(1) == 0 and movimentoj2 == "2" or posicoes.index(4) == 0 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 1
                if posicoes.index(2) == 1 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 1 and (posicoes.index(3) == 4 and movimentoj2 == "2" or posicoes.index(1) == 4 and movimentoj2 == "2" or posicoes.index(4) == 4 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 4
                if posicoes.index(2) == 4 and (posicoes.index(3) == 3 and movimentoj2 == "2" or posicoes.index(1) == 3 and movimentoj2 == "2" or posicoes.index(4) == 3 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 4 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 4 and (posicoes.index(3) == 1 and movimentoj2 == "2" or posicoes.index(1) == 1 and movimentoj2 == "2" or posicoes.index(4) == 1 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()


            elif movimentoj2 == "4":
                if posicoes.index(0) == 2 and posicoes.index(4) == 0 and movimentoj2 == "4":
                    posicoes[0] = 0
                    posicoes[2] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 2 and posicoes.index(0) == 0 and movimentoj2 == "4":
                    posicoes[0] = 4
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 3 and posicoes.index(0) == 2 and movimentoj2 == "4":
                    posicoes[3] = 0
                    posicoes[2] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(4) == 2 and movimentoj2 == "4":
                    posicoes[3] = 4
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 3 and posicoes.index(0) == 0 and movimentoj2 == "4":
                    posicoes[3] = 0
                    posicoes[0] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(4) == 0 and movimentoj2 == "4":
                    posicoes[3] = 4
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 3 and posicoes.index(0) == 4 and movimentoj2 == "4":
                    posicoes[3] = 0
                    posicoes[4] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(4) == 4 and movimentoj2 == "4":
                    posicoes[3] = 4
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 1 and posicoes.index(0) == 2 and movimentoj2 == "4":
                    posicoes[2] = 4
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(4) == 2 and movimentoj2 == "4":
                    posicoes[2] = 0
                    posicoes[1] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 2 and posicoes.index(0) == 4 and movimentoj2 == "4":
                    posicoes[2] = 0
                    posicoes[4] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 2 and posicoes.index(4) == 4 and movimentoj2 == "4":
                    posicoes[2] = 4
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 1 and posicoes.index(0) == 4 and movimentoj2 == "4":
                    posicoes[1] = 0
                    posicoes[4] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(4) == 4 and movimentoj2 == "4":
                    posicoes[1] = 4
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"

                # Avalia posição do 4 na 0
                if posicoes.index(4) == 0 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 0 and (posicoes.index(3) == 3 and movimentoj2 == "4" or posicoes.index(1) == 3 and movimentoj2 == "4" or posicoes.index(2) == 3 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 3
                if posicoes.index(4) == 3 and (posicoes.index(3) == 4 and movimentoj2 == "4" or posicoes.index(1) == 4 and movimentoj2 == "4" or posicoes.index(2) == 4 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 3 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 3 and (posicoes.index(3) == 0 and movimentoj2 == "4" or posicoes.index(1) == 0 and movimentoj2 == "4" or posicoes.index(2) == 0 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 2
                if posicoes.index(4) == 2 and (posicoes.index(3) == 4 and movimentoj2 == "4" or posicoes.index(1) == 4 and movimentoj2 == "4" or posicoes.index(2) == 4 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 2 and (posicoes.index(3) == 1 and movimentoj2 == "4" or posicoes.index(1) == 1 and movimentoj2 == "4" or posicoes.index(2) == 1 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 2 and (posicoes.index(3) == 3 and movimentoj2 == "4" or posicoes.index(1) == 3 and movimentoj2 == "4" or posicoes.index(2) == 3 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 2 and (posicoes.index(3) == 0 and movimentoj2 == "4" or posicoes.index(1) == 0 and movimentoj2 == "4" or posicoes.index(2) == 0 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 1
                if posicoes.index(4) == 1 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 1 and (posicoes.index(3) == 4 and movimentoj2 == "4" or posicoes.index(1) == 4 and movimentoj2 == "4" or posicoes.index(2) == 4 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 4
                if posicoes.index(4) == 4 and (posicoes.index(3) == 3 and movimentoj2 == "4" or posicoes.index(1) == 3 and movimentoj2 == "4" or posicoes.index(2) == 3 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 4 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 4 and (posicoes.index(3) == 1 and movimentoj2 == "4" or posicoes.index(1) == 1 and movimentoj2 == "4" or posicoes.index(2) == 1 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

            else:
                print("\nPor favor, faça um movimento válido! Selecione um número par disponível para movimentar 2 ou 4.")

def jogadorvsmaquina():
    turno = 1
    while not vitoriajogadorvsmaquina():
        if turno % 2 != 0:
            if vitoriajogadorvsmaquina():
                break
            else:
                movimentoj1 = input("\nSua vez Jogador 1.\nPor favor, escolha de acordo com mapa das posições mostrado no começo, uma posição que contenha sua peça para movimentá-la para um espaço válido:\n")

            if movimentoj1 == "1":
                if posicoes.index(0) == 2 and posicoes.index(1) == 0 and movimentoj1 == "1":
                    posicoes[0] = 0
                    posicoes[2] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 2 and posicoes.index(0) == 0 and movimentoj1 == "1":
                    posicoes[0] = 1
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 3 and posicoes.index(0) == 2 and movimentoj1 == "1":
                    posicoes[3] = 0
                    posicoes[2] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(1) == 2 and movimentoj1 == "1":
                    posicoes[3] = 1
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 3 and posicoes.index(0) == 0 and movimentoj1 == "1":
                    posicoes[3] = 0
                    posicoes[0] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(1) == 0 and movimentoj1 == "1":
                    posicoes[3] = 1
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 3 and posicoes.index(0) == 4 and movimentoj1 == "1":
                    posicoes[3] = 0
                    posicoes[4] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(1) == 4 and movimentoj1 == "1":
                    posicoes[3] = 1
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 1 and posicoes.index(0) == 2 and movimentoj1 == "1":
                    posicoes[2] = 1
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(1) == 2 and movimentoj1 == "1":
                    posicoes[2] = 0
                    posicoes[1] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 2 and posicoes.index(0) == 4 and movimentoj1 == "1":
                    posicoes[2] = 0
                    posicoes[4] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 2 and posicoes.index(1) == 4 and movimentoj1 == "1":
                    posicoes[2] = 1
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(1) == 1 and posicoes.index(0) == 4 and movimentoj1 == "1":
                    posicoes[1] = 0
                    posicoes[4] = 1
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(1) == 4 and movimentoj1 == "1":
                    posicoes[1] = 1
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"

                #Aqui tem treta kkkk

                #Avalia posição do 1 na 0
                if posicoes.index(1) == 0 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 0 and (posicoes.index(2) == 3 and movimentoj1 == "1" or posicoes.index(3) == 3 and movimentoj1 == "1" or posicoes.index(4) == 3 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                #Avalia posição do 1 na 3
                if posicoes.index(1) == 3 and (posicoes.index(2) == 4 and movimentoj1 == "1" or posicoes.index(3) == 4 and movimentoj1 == "1" or posicoes.index(4) == 4 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 3 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 3 and (posicoes.index(2) == 0 and movimentoj1 == "1" or posicoes.index(3) == 0 and movimentoj1 == "1" or posicoes.index(4) == 0 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                #Avalia posição do 1 na 2
                if posicoes.index(1) == 2 and (posicoes.index(2) == 4 and movimentoj1 == "1" or posicoes.index(3) == 4 and movimentoj1 == "1" or posicoes.index(4) == 4 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 2 and (posicoes.index(2) == 1 and movimentoj1 == "1" or posicoes.index(3) == 1 and movimentoj1 == "1" or posicoes.index(4) == 1 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 2 and (posicoes.index(2) == 3 and movimentoj1 == "1" or posicoes.index(3) == 3 and movimentoj1 == "1" or posicoes.index(4) == 3 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 2 and (posicoes.index(2) == 0 and movimentoj1 == "1" or posicoes.index(3) == 0 and movimentoj1 == "1" or posicoes.index(4) == 0 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                #Avalia posição do 1 na 1
                if posicoes.index(1) == 1 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 1 and (posicoes.index(2) == 4 and movimentoj1 == "1" or posicoes.index(3) == 4 and movimentoj1 == "1" or posicoes.index(4) == 4 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                #Avalia posição do 1 na 4
                if posicoes.index(1) == 4 and (posicoes.index(2) == 3 and movimentoj1 == "1" or posicoes.index(3) == 3 and movimentoj1 == "1" or posicoes.index(4) == 3 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 4 and (posicoes.index(2) == 2 and movimentoj1 == "1" or posicoes.index(3) == 2 and movimentoj1 == "1" or posicoes.index(4) == 2 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(1) == 4 and (posicoes.index(2) == 1 and movimentoj1 == "1" or posicoes.index(3) == 1 and movimentoj1 == "1" or posicoes.index(4) == 1 and movimentoj1 == "1"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

            elif movimentoj1 == "3":
                if posicoes.index(0) == 2 and posicoes.index(3) == 0 and movimentoj1 == "3":
                    posicoes[0] = 0
                    posicoes[2] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 2 and posicoes.index(0) == 0 and movimentoj1 == "3":
                    posicoes[0] = 3
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 3 and posicoes.index(0) == 2 and movimentoj1 == "3":
                    posicoes[3] = 0
                    posicoes[2] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(3) == 2 and movimentoj1 == "3":
                    posicoes[3] = 3
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 3 and posicoes.index(0) == 0 and movimentoj1 == "3":
                    posicoes[3] = 0
                    posicoes[0] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(3) == 0 and movimentoj1 == "3":
                    posicoes[3] = 3
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 3 and posicoes.index(0) == 4 and movimentoj1 == "3":
                    posicoes[3] = 0
                    posicoes[4] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 3 and posicoes.index(3) == 4 and movimentoj1 == "3":
                    posicoes[3] = 3
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 1 and posicoes.index(0) == 2 and movimentoj1 == "3":
                    posicoes[2] = 3
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(3) == 2 and movimentoj1 == "3":
                    posicoes[2] = 0
                    posicoes[1] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 2 and posicoes.index(0) == 4 and movimentoj1 == "3":
                    posicoes[2] = 0
                    posicoes[4] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 2 and posicoes.index(3) == 4 and movimentoj1 == "3":
                    posicoes[2] = 3
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(3) == 1 and posicoes.index(0) == 4 and movimentoj1 == "3":
                    posicoes[1] = 0
                    posicoes[4] = 3
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"
                if posicoes.index(0) == 1 and posicoes.index(3) == 4 and movimentoj1 == "3":
                    posicoes[1] = 3
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj1 = "0"

                # Avalia posição do 3 na 0
                if posicoes.index(3) == 0 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 0 and (posicoes.index(2) == 3 and movimentoj1 == "3" or posicoes.index(1) == 3 and movimentoj1 == "3" or posicoes.index(4) == 3 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 3
                if posicoes.index(3) == 3 and (posicoes.index(2) == 4 and movimentoj1 == "3" or posicoes.index(1) == 4 and movimentoj1 == "3" or posicoes.index(4) == 4 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 3 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 3 and (posicoes.index(2) == 0 and movimentoj1 == "3" or posicoes.index(1) == 0 and movimentoj1 == "3" or posicoes.index(4) == 0 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 2
                if posicoes.index(3) == 2 and (posicoes.index(2) == 4 and movimentoj1 == "3" or posicoes.index(1) == 4 and movimentoj1 == "3" or posicoes.index(4) == 4 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 2 and (posicoes.index(2) == 1 and movimentoj1 == "3" or posicoes.index(1) == 1 and movimentoj1 == "3" or posicoes.index(4) == 1 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 2 and (posicoes.index(2) == 3 and movimentoj1 == "3" or posicoes.index(1) == 3 and movimentoj1 == "3" or posicoes.index(4) == 3 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 2 and (posicoes.index(2) == 0 and movimentoj1 == "3" or posicoes.index(1) == 0 and movimentoj1 == "3" or posicoes.index(4) == 0 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 1
                if posicoes.index(3) == 1 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 1 and (posicoes.index(2) == 4 and movimentoj1 == "3" or posicoes.index(1) == 4 and movimentoj1 == "3" or posicoes.index(4) == 4 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 3 na 4
                if posicoes.index(3) == 4 and (posicoes.index(2) == 3 and movimentoj1 == "3" or posicoes.index(1) == 3 and movimentoj1 == "3" or posicoes.index(4) == 3 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 4 and (posicoes.index(2) == 2 and movimentoj1 == "3" or posicoes.index(1) == 2 and movimentoj1 == "3" or posicoes.index(4) == 2 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(3) == 4 and (posicoes.index(2) == 1 and movimentoj1 == "3" or posicoes.index(1) == 1 and movimentoj1 == "3" or posicoes.index(4) == 1 and movimentoj1 == "3"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
            else:
                print("\nPor favor, faça um movimento válido! Selecione um número ímpar disponível para movimentar 1 ou 3.")

        if turno % 2 == 0:
            seq = ("2","4")
            if vitoriajogadorvsmaquina():
                break
            else:
                print("\nVez da Máquina!\n")
                movimentoj2 = (random.choice(seq))

            if movimentoj2 == "2":
                if posicoes.index(0) == 2 and posicoes.index(2) == 0 and movimentoj2 == "2":
                    posicoes[0] = 0
                    posicoes[2] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 2 and posicoes.index(0) == 0 and movimentoj2 == "2":
                    posicoes[0] = 2
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 3 and posicoes.index(0) == 2 and movimentoj2 == "2":
                    posicoes[3] = 0
                    posicoes[2] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(2) == 2 and movimentoj2 == "2":
                    posicoes[3] = 2
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 3 and posicoes.index(0) == 0 and movimentoj2 == "2":
                    posicoes[3] = 0
                    posicoes[0] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(2) == 0 and movimentoj2 == "2":
                    posicoes[3] = 2
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 3 and posicoes.index(0) == 4 and movimentoj2 == "2":
                    posicoes[3] = 0
                    posicoes[4] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(2) == 4 and movimentoj2 == "2":
                    posicoes[3] = 2
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 1 and posicoes.index(0) == 2 and movimentoj2 == "2":
                    posicoes[2] = 2
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(2) == 2 and movimentoj2 == "2":
                    posicoes[2] = 0
                    posicoes[1] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 2 and posicoes.index(0) == 4 and movimentoj2 == "2":
                    posicoes[2] = 0
                    posicoes[4] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 2 and posicoes.index(2) == 4 and movimentoj2 == "2":
                    posicoes[2] = 2
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(2) == 1 and posicoes.index(0) == 4 and movimentoj2 == "2":
                    posicoes[1] = 0
                    posicoes[4] = 2
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(2) == 4 and movimentoj2 == "2":
                    posicoes[1] = 2
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"

                # Avalia posição do 2 na 0
                if posicoes.index(2) == 0 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 0 and (posicoes.index(3) == 3 and movimentoj2 == "2" or posicoes.index(1) == 3 and movimentoj2 == "2" or posicoes.index(4) == 3 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 3
                if posicoes.index(2) == 3 and (posicoes.index(3) == 4 and movimentoj2 == "2" or posicoes.index(1) == 4 and movimentoj2 == "2" or posicoes.index(4) == 4 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 3 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 3 and (posicoes.index(3) == 0 and movimentoj2 == "2" or posicoes.index(1) == 0 and movimentoj2 == "2" or posicoes.index(4) == 0 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 2
                if posicoes.index(2) == 2 and (posicoes.index(3) == 4 and movimentoj2 == "2" or posicoes.index(1) == 4 and movimentoj2 == "2" or posicoes.index(4) == 4 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 2 and (posicoes.index(3) == 1 and movimentoj2 == "2" or posicoes.index(1) == 1 and movimentoj2 == "2" or posicoes.index(4) == 1 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 2 and (posicoes.index(3) == 3 and movimentoj2 == "2" or posicoes.index(1) == 3 and movimentoj2 == "2" or posicoes.index(4) == 3 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 2 and (posicoes.index(3) == 0 and movimentoj2 == "2" or posicoes.index(1) == 0 and movimentoj2 == "2" or posicoes.index(4) == 0 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 1
                if posicoes.index(2) == 1 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 1 and (posicoes.index(3) == 4 and movimentoj2 == "2" or posicoes.index(1) == 4 and movimentoj2 == "2" or posicoes.index(4) == 4 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 2 na 4
                if posicoes.index(2) == 4 and (posicoes.index(3) == 3 and movimentoj2 == "2" or posicoes.index(1) == 3 and movimentoj2 == "2" or posicoes.index(4) == 3 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 4 and (posicoes.index(3) == 2 and movimentoj2 == "2" or posicoes.index(1) == 2 and movimentoj2 == "2" or posicoes.index(4) == 2 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(2) == 4 and (posicoes.index(3) == 1 and movimentoj2 == "2" or posicoes.index(1) == 1 and movimentoj2 == "2" or posicoes.index(4) == 1 and movimentoj2 == "2"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

            elif movimentoj2 == "4":
                if posicoes.index(0) == 2 and posicoes.index(4) == 0 and movimentoj2 == "4":
                    posicoes[0] = 0
                    posicoes[2] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 2 and posicoes.index(0) == 0 and movimentoj2 == "4":
                    posicoes[0] = 4
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 3 and posicoes.index(0) == 2 and movimentoj2 == "4":
                    posicoes[3] = 0
                    posicoes[2] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(4) == 2 and movimentoj2 == "4":
                    posicoes[3] = 4
                    posicoes[2] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 3 and posicoes.index(0) == 0 and movimentoj2 == "4":
                    posicoes[3] = 0
                    posicoes[0] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(4) == 0 and movimentoj2 == "4":
                    posicoes[3] = 4
                    posicoes[0] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 3 and posicoes.index(0) == 4 and movimentoj2 == "4":
                    posicoes[3] = 0
                    posicoes[4] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 3 and posicoes.index(4) == 4 and movimentoj2 == "4":
                    posicoes[3] = 4
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 1 and posicoes.index(0) == 2 and movimentoj2 == "4":
                    posicoes[2] = 4
                    posicoes[1] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(4) == 2 and movimentoj2 == "4":
                    posicoes[2] = 0
                    posicoes[1] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 2 and posicoes.index(0) == 4 and movimentoj2 == "4":
                    posicoes[2] = 0
                    posicoes[4] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 2 and posicoes.index(4) == 4 and movimentoj2 == "4":
                    posicoes[2] = 4
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(4) == 1 and posicoes.index(0) == 4 and movimentoj2 == "4":
                    posicoes[1] = 0
                    posicoes[4] = 4
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"
                if posicoes.index(0) == 1 and posicoes.index(4) == 4 and movimentoj2 == "4":
                    posicoes[1] = 4
                    posicoes[4] = 0
                    tabuleiro()
                    turno += 1
                    movimentoj2 = "0"

                # Avalia posição do 4 na 0
                if posicoes.index(4) == 0 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 0 and (posicoes.index(3) == 3 and movimentoj2 == "4" or posicoes.index(1) == 3 and movimentoj2 == "4" or posicoes.index(2) == 3 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 3
                if posicoes.index(4) == 3 and (posicoes.index(3) == 4 and movimentoj2 == "4" or posicoes.index(1) == 4 and movimentoj2 == "4" or posicoes.index(2) == 4 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 3 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 3 and (posicoes.index(3) == 0 and movimentoj2 == "4" or posicoes.index(1) == 0 and movimentoj2 == "4" or posicoes.index(2) == 0 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 2
                if posicoes.index(4) == 2 and (posicoes.index(3) == 4 and movimentoj2 == "4" or posicoes.index(1) == 4 and movimentoj2 == "4" or posicoes.index(2) == 4 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 2 and (posicoes.index(3) == 1 and movimentoj2 == "4" or posicoes.index(1) == 1 and movimentoj2 == "4" or posicoes.index(2) == 1 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 2 and (posicoes.index(3) == 3 and movimentoj2 == "4" or posicoes.index(1) == 3 and movimentoj2 == "4" or posicoes.index(2) == 3 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 2 and (posicoes.index(3) == 0 and movimentoj2 == "4" or posicoes.index(1) == 0 and movimentoj2 == "4" or posicoes.index(2) == 0 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 1
                if posicoes.index(4) == 1 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 1 and (posicoes.index(3) == 4 and movimentoj2 == "4" or posicoes.index(1) == 4 and movimentoj2 == "4" or posicoes.index(2) == 4 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

                # Avalia posição do 4 na 4
                if posicoes.index(4) == 4 and (posicoes.index(3) == 3 and movimentoj2 == "4" or posicoes.index(1) == 3 and movimentoj2 == "4" or posicoes.index(2) == 3 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 4 and (posicoes.index(3) == 2 and movimentoj2 == "4" or posicoes.index(1) == 2 and movimentoj2 == "4" or posicoes.index(2) == 2 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()
                if posicoes.index(4) == 4 and (posicoes.index(3) == 1 and movimentoj2 == "4" or posicoes.index(1) == 1 and movimentoj2 == "4" or posicoes.index(2) == 1 and movimentoj2 == "4"):
                    print("\nEspaço já ocupado! Por isso, não foi possível mover. Tente novamente!\n")
                    tabuleiro()

            else:
                print(
                    "\nPor favor, faça um movimento válido! Selecione um número par disponível para movimentar 2 ou 4.")

print("[" + str(posicoes[0]) + "]\     /[" + str(posicoes[1]) + "]\n |   [" + str(posicoes[2]) + "]   | \n[" + str(posicoes[3]) + "]/-----\[" + str(posicoes[4]) + "]")

if tipojogar == "1":
    jogadorvsmaquina()

elif tipojogar == "2":
    jogadorvsjogador()
