import random


def coin_flip(k,a):
    syt=0
    syh=0
    if k>=0:
        if a=="T" or a=="H":
            if a=="T":
                while 0<1:
                    if k==0:
                        print("You got T "+str(syt)+" times in a row!")
                        break
                    chan=random.randint(1,2)
                    if chan==1:
                        if syt==k:
                            print()
                            print("You got T "+str(syt)+" times in a row!")
                            break
                        print("T ",end="")
                        syh=0
                        syt=syt+1
                    elif chan==2:
                        print("H ",end="")
                        syt=0
                        syh=syh+1
            if a=="H":
                while 0<1:
                    if k==0:
                        print("You got H "+str(syt)+" times in a row!")
                        break
                    chan=random.randint(1,2)
                    if chan==2:"
                        if syh==k:
                            print()
                            print("You got H "+str(syh)+" times in a row!")
                            break
                        print("H ",end="")
                        syt=0
                        syh=syh+1
                    elif chan==1:
                        print("T ",end="")
                        syt=syt+1
                        syh=0
        else:
            print("ERROR!")
    else:
        print("ERROR!")
                
        
    
        

    

def main():
    k=4
    a="T"
    coin_flip(k,a)
main()