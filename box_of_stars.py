def box_of_stars(w, h):
    for i in range(0,h):
        if i == 0 or i == h-1:
            for j in range(0,w):
                print("*", end="")
        else:
            for k in range(0,w):
                if k == 0 or k == w-1:
                    print("*",end="")
                else:
                    print(" ",end="")
        print()
               






def main():
    w=8
    h=5
    box_of_stars(w, h)
main()