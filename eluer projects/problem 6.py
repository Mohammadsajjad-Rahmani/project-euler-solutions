from time import time
start = time()
sum = 0
for i in range(1,101):
    sum+=i**2
sum_2 = 0
for j in range(1,101):
    sum_2+=j
print(sum_2**2-sum)
end = time()
print(f"Execute time : {end - start}")