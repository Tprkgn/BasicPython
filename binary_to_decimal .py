def binary_to_decimal(number):
    first = 0
    num2= number
    top=0
    while num2>0:
        a=num2%10
        top=top+(a)*(2**first)
    
        first = first+1
        num2=int(num2/10)
    return top

def main():
    number= 10000

    print(binary_to_decimal(number))
main()