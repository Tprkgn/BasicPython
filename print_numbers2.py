def print_numbers2():
    s=1
    s2=s
    b=4
    for s in range(s,6):
        if b!=0:
            for b in range(1,b+1):
                print(".",end="")
            b=b-1
        for s in range(s,s+1):
            if s2!=6 and s==s2:
                for s in range(s,s+s):
                    print(s2,end="")
                s2=s2+1
        s=s+1
        print()
def main():
    print_numbers2()
main()