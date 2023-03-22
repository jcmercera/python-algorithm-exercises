# our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16

# How can we get ones of a number?
# We can use modulus and divide the number by 10: 12 % 10 = 2

# How to get tens and hundreds of a number?
# We need to get rid of the ones. We divide a number by 10 and get rid of the remainder.
# For example: if the number is 125, we need to get rid of 5. We divide 125 //10 = 12 (get rid of 0.5)
# We use modulus to get number we need 12 % 10 = 2
# And then repeat for hundreds.


# code here

def sum_of_digits_numbers(n: int):
    result = 0
    original_n = n
    while n != 0:  # while number is NOT equal to 0
        result += (n % 10)
        n = n // 10

    print(f"Sum of all digits in {original_n} is {result}")


test_number = 12568765
sum_of_digits_numbers(test_number)
