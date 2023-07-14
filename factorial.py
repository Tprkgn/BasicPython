def factorial(n):
    top=1
    for i in range(n,0,-1):
        top=top*i
    print(str(n)+" factorial = "+str(top))
    
def main():
    n=4
    factorial(n)
main()