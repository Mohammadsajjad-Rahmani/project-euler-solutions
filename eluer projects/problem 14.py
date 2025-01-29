


def collatz_term(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_n(n):
    # lookup table for previously found Collatz sequence lengths
    lookup = {
        1: 1}  # Initialise with first term so check_collatz works separately, there may be a better way to implement this

    # Finds the length of the Collatz sequence for number and all following terms
    def check_collatz(number):
        seq_len, prev_nums = 0, []
        if number <= 0:  # Quick check to exclude non-positive integers.
            return 0
        if number == 1:
            lookup[1] = 0
            return 0

        while number not in lookup:
            prev_nums.append(number)
            number = collatz_term(number)
            seq_len += 1

        seq_len += lookup[number]
        for prev_num in prev_nums:
            lookup[prev_num] = seq_len  # saves all the previous obtained Collatz terms into lookup
            seq_len -= 1
        if prev_nums == []:
            return number
        else:
            return lookup[prev_nums[0]]

    # Generates the length of the Collatz sequences for 1 to n - 1
    for k in range(1, n):
        check_collatz(k)

    largest_collatz = max(lookup, key=lookup.get)

    return (largest_collatz, lookup[largest_collatz]+1)


inp_collatz = int(input("Input the number you would like to check to : "))

print(collatz_n(inp_collatz))
