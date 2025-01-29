from time import time
def check_number(number):
    flag = True
    temp = int(number**0.5)
    prime_list = []
    for item in range(2,temp):
        flag = True
        if number % item == 0 :
            for element in range(2,int(item/2)):
                if item % element == 0:
                    flag = False
            if flag == True:
                prime_list.append(item)
    print(f"The list of prime divisible numbers : {prime_list}")
    print(f"Maximum of the list : {max(prime_list)}")
start_time = time()
check_number(600851475143)
end_time = time()
print(f"execute time : {end_time - start_time} ")