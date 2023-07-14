def print_numbers1():
    s=1
    s2=s
    for s in range(s,6):
        for s in range(s,s+1):
            if s2!=6 and s==s2:
                for s in range(s,s+s):
                    print(s2,end="")
                s2=s2+1
        s=s+1
        print()
def main():
    print_numbers1()
main()
        
