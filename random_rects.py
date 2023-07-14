def random_rects():
    ds = int(input("How many rectangles? "))
    a=1
    sum=0
    for i in range(0,ds) :
        
        print("Width " + str(a)+"?" , end=" ")
        w = int(input())
        
        print("Height " + str(a)+"?" , end=" ")
        h = int(input())

        a+=1
        sum += w*h
        for j in range(0,h):
            for k in range(0,w):
                print("*",end="")
            print()      
    print("Total area: "+str(sum))
            

        




def main():
    random_rects()
main()