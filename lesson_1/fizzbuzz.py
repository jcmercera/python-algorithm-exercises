# Print integers one-to-N, but print “Fizz” if an integer is divisible by three,
# “Buzz” if an integer is divisible by five, and “FizzBuzz” if an integer is divisible by both three and five.
# Other wise print the number.

def fizzbuzz(n: int):
    for i in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print('FrizzBuzz')
        elif n % 3 == 0:
            print('Frizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(i)


n = 4862
fizzbuzz(n)
