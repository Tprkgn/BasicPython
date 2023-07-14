def print_triangle():
    s=1
    
    for s in range(s,7):
        for x in range(1,s+1):
            print("#",end="")       
        s=s+1
        print()
        
def main():
    print_triangle()
main()