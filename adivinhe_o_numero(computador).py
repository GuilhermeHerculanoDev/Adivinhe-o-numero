import random
import time

def jogo():
    numero_aleatorio = round(random.random()*100)
    print(numero_aleatorio)
    time.sleep(1)
        
    while True:
        numero = int(input("Tente acerta o número: "))
        if numero > numero_aleatorio:
            print("Você errou :( O número é menor: ")
        elif numero < numero_aleatorio:
            print("Você errou :( O número é maior: ")
        else:
            print("Parabens, você acertou!!!")
            jogaNovamente()
            break

    
def jogaNovamente():
    time.sleep(1)
    jogar_Novamente = input("Deseja jogar novamente?" "\n" "S = Sim; N = Não: ")

    if jogar_Novamente == 'S':
        jogo()
    elif jogar_Novamente == 'N':
        print("Adeus :(")
    else:
        print("Vou entender isso como um não")

def Jogar():
    print("Bem-vindo ao jogo!!!")
    time.sleep(1)
    print("Nesse jogo você tentará acertar um número aleatório entre 1 e 100.")
    time.sleep(1)
    print("Aguarde um momento, o computador está gerando um número...")
    time.sleep(2)
    jogo()

Jogar()