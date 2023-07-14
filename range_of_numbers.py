from os import sep


def range_of_numbers(a, b):
    if a<b :
        for a in range(a,b+1):
            print(a,end=" ")
    else :
        for a in range(a,b-1,-1):
            print(a,end=" ")
def main():
    a=int(input())
    b=int(input())
    range_of_numbers(a, b)   
main()