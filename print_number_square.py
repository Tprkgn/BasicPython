def print_number_square(min, max):
    difference = max-min+1
    start = min

    for i in range(difference):

        for j in range(difference):
            print(start, end="")
            start+=1
            if start == max+1:
                start = min

        start = start+1
        print()


def main():
    min =3
    max = 7
    print_number_square(min, max)
main()
