def prime():
    sum = 2
    c = 0
    for n in range(3, 2000000):
        for m in range(2, int(n ** 0.5 + 1)):
            if n % m == 0:
                c = 1
                break
        if c == 0:
            sum += n
        else:
            c = 0
    return sum


print(prime())
