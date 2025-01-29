def multiple():
    list_palindromic = []
    for number_1 in range(100,1000):
        for number_2 in range(100,1000):
            result = number_1 * number_2
            if palindromic(result) :
                list_palindromic.append(result)
    print(max(list_palindromic))
def palindromic(number):
    power = -1
    reverse_number = 0
    save_number = number
    number_2 = number
    while(number_2 > 0):
        number_2 = int(number_2/10)
        power+=1
    while(number>0):
        mode_number = number%10
        number = int(number/10)
        sum = mode_number * 10 ** power
        reverse_number+=sum
        power-=1
    if reverse_number == save_number:
        return True
    else:
        return False

multiple()


