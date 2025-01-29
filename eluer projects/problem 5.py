from time import time
start = time()
# def divide(number):
#     def div_6(number):
#         last_digit = number % 10
#         if (last_digit % 2 == 0):
#             sum = 0
#             for digit in str(number):
#                 sum += int(digit)
#             if (sum % 3 == 0):
#                 return False
#             else:
#                 return True
#     if (div_6(number)):
#         return False
#     else:
#         def div_8(number):
#             str_number = str(number)
#             rev_str_1 = str_number[:-4:-1]
#             rev_str_2 = rev_str_1[::-1]
    #         rev_str_2 = int(rev_str_2)
    #         if (rev_str_2 % 8 == 0):
    #             return False
    #         else:
    #             return True
    # if (div_8(number)):
    #     return False
    # else:
    #     def div_10(number):
    #         if (number % 10 == 0):
    #             return False
    #         else:
    #             return True
    # if (div_10(number)):
    #     return False
    # else:
    #     def div_11(number):
    #         str_number = str(number)
    #         set_1 = str_number[::2]
    #         set_2 = str_number[1::2]
    #         sum_1 = 0
    #         sum_2 = 0
#             for digit in set_1:
#                 sum_1 += int(digit)
#             for digit in set_2:
#                 sum_2 += int(digit)
#             result = sum_1 - sum_2
#             if (result % 11 == 0):
#                 return False
#             else:
#                 return True
#     if (div_11(number)):
#         return False
#     else:
#         def div_12(number):
#             sum = 0
#             for digit in str(number):
#                 sum += int(digit)
#             if (sum % 3 == 0):
#                 str_number = str(number)
#                 number_2 = str_number[:-3:-1]
#                 number_2 = number_2[:-3:-1]
#                 number_2 = int(number_2)
#                 if (number_2 % 4 == 0):
#                     return False
#             else:
#                 return True
#     if (div_12(number)):
#         return False
#     else:
#         def div_13(number):
#             last_digit = number % 10
#             new_number = number / 10
#             result = new_number + 4 * last_digit
#             if (result % 13 == 0):
#                 return False
#             else:
#                 return True
#     if (div_13(number)):
#         return False
#     else:
#         def div_14(number):
#             last_digit = number % 10
#             if (last_digit % 2 == 0):
#                 last_digit = number % 10
#                 new_number = number / 10
#                 result = new_number - 2 * last_digit
#                 if (result % 7 == 0):
#                     return False
#                 else:
#                     return True
#             else:
#                 return True
#     if (div_14(number)):
#         return False
#     else:
#         def div_15(number):
#             sum = 0
#             for digit in str(number):
#                 sum += int(digit)
#             if (sum % 3 == 0):
#                 last_digit = number % 10
#                 if (last_digit % 5 == 0):
#                     return False
#                 else:
#                     return True
#             else:
#                 return True
#     if (div_15(number)):
#         return False
#     else:
#         def div_16(number):
#             str_number = str(number)
#             rev_str = str_number[:-5:-1]
#             rev_str = int(rev_str[::-1])
#             if (rev_str % 16 == 0):
#                 return False
#             else:
#                 return True
#     if (div_16(number)):
#         return False
#     else:
#         def div_17(number):
#             last_digit = number % 10
#             new_number = number / 10
#             result = new_number - 5 * last_digit
#             if (result % 17 == 0):
#                 return False
#             else:
#                 return True
#     if (div_17(number)):
#         return False
#     else:
#         def div_18(number):
#             last_digit = number % 10
#             if (last_digit % 2 == 0):
#                 sum = 0
#                 for digit in str(number):
#                     sum += int(digit)
#                 if (sum % 9 == 0):
#                     return False
#                 else:
#                     return True
#             else:
#                 return True
#     if (div_18(number)):
#         return False
#     else:
#         def div_19(number):
#             last_digit = number % 10
#             new_number = number / 10
#             result = new_number + 2 * last_digit
#             if (result % 19 == 0):
#                 return False
#             else:
#                 return True
#     if (div_19(number)):
#         return False
#     else:
#         def div_20(number):
#             str_number = str(number)
#             rev_str = str_number[:-3:-1]
#             rev_str = int(rev_str[::-1])
#             if (rev_str % 20 == 0):
#                 return True
#             else:
#                 return False
#     if (div_20(number)):
#         return True
#
#
# def creat_number():
#     number = 1000
#     while (True):
#         if (divide(number)):
#             print(number)
#             break
#         else:
#             number += 1
#
#
# creat_number()
def check(number):
    for i in range(11,20):
        if number%i!=0:
             return False
    return True
number = 20
while True:
    if check(number):
        break
    number+=20
print(number)
end = time()
print(f"Execute time : {end - start}")
