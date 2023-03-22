# when user enters a number, its factorial is displayed
# 5! = 1 * 2 * 3 * 4 * 5
#O(n)

def factorial(number: int):
    result = 1
    for i in range(2, number + 1):
        result *= i

    print(f"Factorial of {number} is {result}")


test_number = 8
factorial(test_number)
