# A)
for i in range(5):
    for j in range(10):
        print("*", end="")
    print()   # to end the line
# B)
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# C)
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print("")

