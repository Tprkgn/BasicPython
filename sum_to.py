def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n=5
print(sum_to(n))