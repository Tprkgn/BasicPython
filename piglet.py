import random


def main():
    print("Welcome to Piglet!")
    puan = 0
    s="Yes"
    isyes = True
    while isyes:
        zar = zar = int(((random.random())*6)+1)
        if zar!=1:
            print("You rolled a " + str(zar))
            puan=puan+zar
        else:
            print("You rolled a " + str(zar))
            puan =0
            print("You got " + str(puan)+ " points.")
            break
        s = input("Roll again? ")
        if s == "yes":
            isyes=True
        else:
            isyes=False
            print("You got " + str(puan)+ " points.")
            break



main()