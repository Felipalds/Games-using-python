import random
from playsound import playsound

from time import sleep
print("\033[36mPEDRA\033[m,\033[35m PAPEL\033[m, \033[33mTESOURA \033[m!")
print(30*"\033[31m=\033[m")

c = int(5) #contador para o numero de jogadas <-
while c > 0:
    print("ESCOLHA SUA JOGADA:")
    print("\033[36m[1] PEDRA\033[m")
    print("\033[35m[2] PAPEL\033[m")
    print("\033[33m[3] TESOURA\033[m")
    jog = int(input())

    print("\033[36m JO\033[m")
    sleep(0.5)
    print("\033[35m KEN\033[m")
    sleep(0.5)
    print("\033[33m PO \033[m")
    sleep(1.3)
    print(30*"=")

    jogcom = random.randint(1,3)
    #pedra
    if jog == 1 and jogcom == 1:
        print("\033[30m EMPATE!\033[m ")
        print("mSUA JOGADA: PEDRA")
        print("JOGADA DO CPU: PEDRA")
        sleep(2)
        print(1000 * " ")
        print(30 * "=")

    elif jog == 1 and jogcom == 2:
        print("\033[31mDERROTA!\033[m ")
        print("SUA JOGADA: PEDRA")
        print("JOGADA DO CPU: PAPEL")
        playsound("perdeu.mp3")
        print(1000 * " ")
        print(30 * "=")

    elif jog == 1 and jogcom == 3:
        print("\033[32mVITÓRIA!\033[m")
        print("SUA JOGADA PEDRA")
        print("JOGADA DO CPU: TESOURA")
        playsound("ganhou.mp3")
        print(1000 * " ")
        print(30 * "=")

#papel
    if jog == 2 and jogcom == 2:
        print("\033[30m EMPATE!\033[m ")
        print("SUA JOGADA: PAPEL")
        print("JOGADA DO CPU: PAPEL")
        sleep(2)
        print(1000 * " ")
        print(30 * "=")
    elif jog == 2 and jogcom == 3:
        print("\033[31mDERROTA!\033[m ")
        print("SUA JOGADA: PAPEL")
        print("JOGADA DO CPU: TESOURA")
        playsound("perdeu.mp3")
        print(1000 * " ")
        print(30 * "=")

    elif jog == 2 and jogcom == 1:
        print("\033[32mVITÓRIA!\033[m")
        print("SUA JOGADA: PAPEL")
        print("JOGADA DO CPU: PEDRA")
        playsound("ganhou.mp3")
        print(1000 * " ")
        print(30 * "=")


#tesoura
    if jog == 3 and jogcom == 3:
        print("\033[30m EMPATE!\033[m ")
        print("SUA JOGADA: TESOURA")
        print("JOGADA DO CPU: TESOURA")
        sleep(2)
        print(1000 * " ")
        print(30 * "=")
    elif jog == 3 and jogcom == 1:
        print("\033[31mDERROTA!\033[m ")
        print("SUA JOGADA: TESOURA")
        print("JOGADA DO CPU: PEDRA")
        playsound("perdeu.mp3")
        print(1000 * " ")
        print(30 * "=")

    elif jog == 3 and jogcom == 2:
        print("\033[32mVITÓRIA!\033[m")
        print("SUA JOGADA: TESOURA")
        print("JOGADA DO CPU: PAPEL")
        playsound("ganhou.mp3")
        print(1000 * " ")
        print(30 * "=")

#caso invalido
    if jog != 1 and jog != 2 and jog != 3:
        print("LANCE INVÁLIDO!")
        print(1000 * " ")
        print(30 * "=")