# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
# code here

def sum_of_digits(n: int):
    result = 1

    for i in range(2, n + 1):
        result += i
    print(f'Sum of digits of all numbers of {n} is {result}')


test_number = 9
sum_of_digits(test_number)


# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.
# code here

# def max_number(n: int):
# I don't know how to proceed here


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odd_and_even_numbers(n: int):
    result_odd = 0
    result_even = 0

    for i in range(0,6):
        if i % 3 == 0:
            result_odd += i
            print(f'Sum of all odd numbers {result_odd}')
        elif i % 2 == 0:
            result_even += i
            print(f'Sum of all even numbers {result_even}')


test_numbers = 34560
count_odd_and_even_numbers(test_numbers)

#