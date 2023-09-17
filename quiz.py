from time import sleep
from funcoes import *


while True:
    print("Seja muito bem vindo ao quiz do Kauã")
    answer_user = input("Quer começar? (S/N)").upper()

    if answer_user == "S":
        loading_animation()
        score = 0 #variável que vai guardar as pontuações
        break
    elif answer_user == "N":
        print("Programa encerrado")
        quit()
    else:
        print("Opção inválida! Tente novamente")

print("Quem desenvolveu o jogo (GTA)? \n (A) Rockstar games \n (B) Valve \n (C) Microsoft Studios \n (D) Supercell")
answer_1 = input("Resposta: ").upper()

if answer_1 == "A":
    print("Correto \n")
    score = score + 1 #somar e guardar ponto na variável score
else:
    print("Incorreto")

print("Qual o nome do protagonista do GTA San Andreas? \n (A) Douglas \n (B) Pedro o macaco \n (C) Kleiton \n (D) CJ")
answer_2 = input("Resposta: ").upper()

if answer_2 == "D":
    print("Correto")
    score = score + 1
else:
    print("Incorreto")

loading_animation_finish()
print(f"O quiz acabou! pontuação: {score}/2")
