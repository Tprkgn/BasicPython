def armstrong_numbers(n):
    start = 1
    
    top=0
    if n!=0:
        for i in range(n-1):
            start = start*10

        for i in range(start, start*10+1):
            if top == i-1:
                print(top,end=" ")
            top=0    
            while i>0:
                top=(top+((i%10)**n))
                i=int(i/10)
    else:
        print(end="")  
        
            
        
    





def main():
    n=3
    armstrong_numbers(n)
main()