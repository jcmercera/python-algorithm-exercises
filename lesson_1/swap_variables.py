# User inputs tow numbers. One number is assinged to a variable, the other is assigned to another variable
# the task is to inver the varialbes, so that the first variable contains the second number, while the first numberer
# is in the second varialbe.

# code here
#O(1)
def swamp_variables(a: int, b: int):
    print(f'Before swap: a = {a}, b = {b}')
    a, b = b, a

    # temp = a
    # a = b
    # b = temp

    # a = a + b
    # b = a - b
    # a = a - b

    print(f'After swap: a = {a}, b = {b}')


test_a = 51
test_b = 10
swamp_variables(test_a, test_b)
