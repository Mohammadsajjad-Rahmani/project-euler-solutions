
def fibo_sequence():
    fib_1 = 1
    fib_2 = 2
    new_fib = 0
    while(new_fib<4000000):
        new_fib = fib_1 + fib_2
        fib_1 = fib_2
        fib_2  = new_fib
        if fib_1%2==0:
            yield fib_1
print("summation result is :" , sum(fibounachi_sequence))
