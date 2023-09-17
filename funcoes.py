from time import sleep

def loading_animation():
    for i in range(4):
        print("Carregando" + "." * i, end = "\r") #A função end="\r" faz com que a função print substitua a linha anterior a cada iteração
        sleep(0.5)

def loading_animation_finish():
    for i in range(4):
        print("Processando" + "." * i , end = "\r") #A função end="\r" faz com que a função print substitua a linha anterior a cada iteração
        sleep(0.5)