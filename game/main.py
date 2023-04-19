import random


def run():
    numero = int(input(" Escribe un numero del 1 al 100  "))
    num_random = random.randint(1,100)
    while numero != num_random:
        if numero < num_random:
            print(" ingresa un numero mayor")
        else:
            print("ingresa numero menor")
        numero = int(input("ingresa otro numero "))        
    print("!Ganaste")  

if __name__=="__main__":
    run() 