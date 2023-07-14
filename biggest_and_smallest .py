def main():
    a =int(input("How many numbers? "))
    list=[]
    for i in range(0,a):
        list.insert(i,int(input("Next number? ")))
    biggest =  max(list)
    smallest = min(list)
    print("Biggest = " + str(biggest)+"\nSmallest = " + str(smallest))
    






main()