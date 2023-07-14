def print_wave():
    rows = 5
    
    for i in range(-2, rows+2):
        for j in range(-1, i + 2,2):
            print("v", end='')
        print()
    
    for i in range(rows, -3, -1):
        for j in range(-1,i+2,2):
            print("v", end='')
        print()
def main():
    print_wave()
main()