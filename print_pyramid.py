def print_pyramid():
    r=100
    b=100
    a=1
    for x in range(1,r+1):
        for y in range(b):
            print(" ",end="")
        for z in range(a):
            print("*",end="")
        print()
        b=b-1
        a=a+2

def main():
    print_pyramid()
main()