import random
from time import sleep

def dado(min, max):
    return random.randint(min,max)

print ("Ola")
sleep(1)
print ("Bem vindo ao dado digital")
print ("Qual seu nome?")
nome = input(str())
sleep(1)
print (f"{nome}, hmmm que nome bonito")
print (f"Entao {nome} deseja jogar o dado? digite 'sim' ou 'nao'")
sleep(1)
condicional = input(str())

if condicional == "sim":

    while True:
        resultado = dado(1, 6)
        print (f"Bom, o dado parou em {resultado}")
        sleep(1)
        print ("mais uma rodada? digite 'sim' ou 'nao'")
        condicional_2 = input(str())
        if condicional_2 == "sim":
            continue
        else:
            print ("ok byee")
            break
