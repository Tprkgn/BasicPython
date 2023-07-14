import random


def random_walk():
    position=0
    move=0
    maxposition = position
    while position != 3 or position != -3:
        if position > maxposition:
            maxposition = position
        
        print("position = "+ str(position))
        rmove=random.randint(1,2)
        
        if rmove == 1:
            move = 1
        else:
            move = -1

        position= position+move
        if position == 3 or position == -3:
            print("position = "+ str(position))
            if position == 3:
                maxposition=3
            break
    print("max position = "+str(maxposition))



def main():
    random_walk()
main()