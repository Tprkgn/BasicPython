def print_numbers3():
    s=1
    s2=s
    b=4
    bs=0
    for s in range(s,6):
        if b!=0:
            for b in range(1,b+1):
                print(".",end="")
            b=b-1
        elif b== 0:
            b=b-1            
        for s in range(s,s+1):
            if s2!=6 and s==s2:
                print(s2,end="")
                s2=s2+1
        s=s+1

        for bs in range(bs,5):
            if b<3:
                for x in range(1,4-b):
                    print(".",end="")

        print()
        
        

def main():
    print_numbers3()
main()