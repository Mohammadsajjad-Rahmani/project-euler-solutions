list = (number for number in range(3,1000) if number%3==0 or number%5==0)
print(sum(list))

def check_function():
    total = 0
    for number in range(3,1000):
        if(number%3==0 or number%5==0):
            total+=number
    yield total
print(next(check_function()))


