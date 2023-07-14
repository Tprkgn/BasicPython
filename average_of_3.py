def average_of_3(n1, n2, n3):
    list = [n1,n2,n3]
    top = 0
    for i in list:
        top = top+i
    return top/3
def main():
    n1 = 4
    n2 = 7
    n3 = 13
    average_of_3(n1, n2, n3)
main()