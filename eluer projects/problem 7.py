def prime(number):
    prime_flag = True
    for i in range(2, int(number**0.5+1)):
        if number % i == 0:
            prime_flag = False
    return prime_flag


def creat():
    counter = 0
    number = 2
    while True:
        if prime(number):
            counter += 1
            if counter == 10001:
                print(number)
                break
        number += 1


creat()