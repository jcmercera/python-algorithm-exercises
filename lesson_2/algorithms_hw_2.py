# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.

string = ""


def split_and_swap(string):
    len_string = len(string)
    first_half_string = string[0:len_string // 2]
    second_half_string = string[len_string // 2:]
    print("String First Half :", first_half_string)
    print("String Second Half:", second_half_string)
    swapped_first_half_string, swapped_second_half_string = second_half_string, first_half_string
    print("Swapped strings:", swapped_first_half_string + swapped_second_half_string)


test_string = "aaaaaabbbbbb"
print("Test string:", test_string)
split_and_swap(test_string)


# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


def split_swap_at_odd(s):
    str_list = s.split("c")
    print(str_list)

    first_half, second_half = str_list[0], str_list[1]
    print("Split swapped halves:", first_half + second_half)


test_odd_string = "ttttttcrrrrr"
result = split_swap_at_odd(test_odd_string)
print(result)


#### Note: I was trying to figure out a way to do this in a loop "if there's an odd character then split it there"
#### could not figure out how. Also how do we store a deleted value to use it again in the future?


# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def unique_char(string):
    char = []
    for c in string:
        if c in char:
            return False
        else:
            return True


test_char = "asdfghhjkl"
result = unique_char(test_char)
print(result)

