import math
summation = 0
for i in range(1, 10 ** 100):
    for j in range(1, i + 1):
        summation += j
    divs = [x for x in range(1, int(math.sqrt(summation))+1) if summation % x == 0]
    opps = [int(summation / x) for x in divs]
    if len(divs + opps) > 500:
        print(f"first triangle number with over 500 hundred divisors --> {summation}")
        print(f"list of divisors --> {sorted(divs + opps)}  \n---> divisors len : {len(divs + opps)}")
        break
    div_counter = 0
    summation = 0
