# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
# code here

# def sum_of_digits(n):
#     final_sum = 0
#     for i in range(n + 1):
#         final_sum += i
#     print(f'Sum of digits of all numbers of {n} is {final_sum}')


def sum_of_numbers(n: int):  # another way of coding it
    final_sum = (n * (n + 1)) / 2
    print(f'Sum of digits of all numbers of {n} is {final_sum}')


test_number = 9
sum_of_numbers(test_number)


# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.
# code here

def max_number(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c


result = max_number(23, 57, 89765)
print(result)


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odd_and_even(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1

        n = n // 10

    print(f"Odd digits: {odds}")
    print(f"Even digits: {evens}")


test_n = 35680
count_odd_and_even(test_n)
