def check(m, n):
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = n ** 2 + m ** 2
    if a + b + c == 1000:
        print(f"m = {m} \nn = {n} \na = {a} \nb = {b} \nc = {c}")
        print(f"value of product : {a * b * c}")
        return True


for n in range(1, 50):
    for m in range(n + 1, 50):
        if check(m, n):
            break
