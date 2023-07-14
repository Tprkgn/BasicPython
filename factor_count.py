def factor_count(n):
    factor=1
    count=0
    for i in range(factor,n+1):
        
        if (n%i)==0 :
            count = count + 1
            
    return count




def main():
    n = 24
    print(factor_count(n))
main()