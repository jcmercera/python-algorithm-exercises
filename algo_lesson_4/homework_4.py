# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


even_odd_list = [3, 4, 33, 76, 62, 9, 87, 66, 90, 23, 1, 200]
even_odd_list.sort(key=lambda nr: nr % 2 != 0)
print('Even and odd list:', even_odd_list)


# Increment a Number
# Write a program that takes as input a list of digits encoding a
# non negative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def plus_one_list(digits):
    carry = 1
    n = len(digits)

    for i in range(n - 1, -1, -1):
        digits[i] += carry
    return digits


test_list = [3, 4, 9, 1, 2, 5, 8]
results = plus_one_list(test_list)
print(test_list)
