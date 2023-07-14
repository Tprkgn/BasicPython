def first_digit(n):
    if n<0:
        n=n*-1
    n2=n
    while n2>1:
        n2=n2/10
        if n2<1:
            n2=n2*10
            break
    return int(n2)



def main():
    n=3572
    first_digit(n)
main()