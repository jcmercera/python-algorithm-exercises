# # escaping characters (\) are used to escape characters in a Python string.
# # For example: to print a string with quotation marks, the given code snippet can be used
#
str = "This is my \"string\""
print(str)

# # the 'in' syntax: is used to determine if a letter or a substring exists in a string.
# # It returns True if a match is found, otherwise False is returned.

str = "This is my string"
print("string" in str)
print("my" in str)
print("be" in str)

# # #Python strings can be indexed using the same notation as lists, since strings are lists of characters.
# # # A single character can be accessed with bracket notation ([index]), or a substring can be accessed using
# # slicing ([start:end]).
# # Indexing with negative numbers counts from the end of the string.
#
# # str = 'yellow'
# # str[1]
# # str[-1]
# # str[4:6]
# # str[:4]
# # str[-3:]
#
str = "This is my string"
print(str[1])
print(str[:4])
print(str[-1])

# # String Concatenation
# # To combine the content of two strings into a single string, Python provides the + operator. This process
# # of joining strings is called concatenation.
#
str1 = "This is my string"
str2 = "and this is my second string"

print(str1 + str2)



# # Iterate String
# # To iterate through a string in Python, “for...in” notation is used.
# #
str1 = "This is my string"
str2 = "and this is my second string"
for char in str1:
    print(char)



# # String Method len()
# # In Python, the built-in len() function can be used to determine the length of an object. It can be used to
# # compute the length of strings, lists, sets, and other countable objects.
#
str1 = "This is my string"
str2 = "and this is my second string"
print(len(str1))




# # String Method .lower()
# # The string method .lower() returns a string with all uppercase characters converted into lowercase.

str1 = "This is my string"
str2 = "and this is my second string"
print(str2.lower())



# # String Method .upper()
# # The string method .upper() returns the string with all lowercase characters converted to uppercase.

str1 = "This is my string"
str2 = "and this is my second string"
print(str1.upper())



# # String Method .split()
# # The string method .split() splits a string into a list o! items:
# # if no argument is passed, the default behavior is to split on whitespace
# # if an argumAnt is passed to the method, that value is used as the delimiter on which to split the string.
# # meaning, the value is deleted and a split is inserted in it's place

str1 = "This is my string"
str2 = "and this is my second string"
print(str1.split())
print(str2.split("i"))




# # String Method .join()
# # The string method &join() concatenates a list of strings together to create a new string joined with the
# # desired delimiter.

str1 = "This is my string"
str2 = "and this is my second string"
print(" - ".join(["first item", "second item", "third item"]))



# # String Method .strip()
# # The string method .strip() can be used to remove characters from the beginning and end of a string.
# # A string argument can be passed to the method, specifying the set of characters to be stripped. With no
# # arguments to the method, whitespace is removed.

str1 = "This is my stringTT"
str2 = "and this is my second string"
print(str1)
print((str1.strip("T")))



# # String Method .replace()
# # The .replace() method is used to replace the occurrence of the first argument with the second argument
# # within the string.

str1 = "This is my string"
str2 = "and this is my second string"
print(str1.replace("i", "o"))



# # String Method .find()
# # The Python string method .find() returns the index of the first occurrence of the string passed as the
# # argument. It returns -1 if no occurrence is found.
#
# str1 = "This is my string"
# str2 = "and this is my second string"
# print(str1.find("i"))
#
# # String Method .format()
# # The Python string method .format() replaces empty brace ({}) placeholders in the string with its
# # arguments.
#
# str1 = "This is my string"
# str2 = "and this is my second string"
# str_format = "This is value {} and this is value {}"
# print(str_format(5, "six"))
#
#
# # Reverse integer
# # Given an integer, return the integer with reversed digits.
# # Note: The integer could be either positive or negative.
#
# def reverse_integer(x):
#     string = str(x)
#
#     if string[0] == '-':
#         return int('-' + string[:0:-1])
#     else:
#         return int(string[::-1])
#
#
# test_x_pos = 123
# test_x_neg = -987
# print(reverse_integer(test_x_pos))
# print(reverse_integer(test_x_neg))


# # Palindrome
# # Given a string, write a python function to check if it is palindrome or not.
# # A string is said to be palindrome if the reverse of the string is the same as string.
# #
# # For example, “radar” is a palindrome, but “radix” is not a palindrome.


def is_palindrome(s):
    return s == s[::-1]
    if s == reverse_s:
        return True
    else:
        return False


test_str_pos = "radar"
test_str_neg = "radar"
result_pos = is_palindrome(test_str_pos)
print(result_pos)

result_neg = is_palindrome(test_str_neg)
print(result_neg)

# # Reverse string
# # Given a string. Return a reversed string.
# # For example, abcde -> edcba.
#
string = "abcdef"
print(string[::-1])


###### COMMON CODING CHALLENGE #################
# Anagram
# Write a function to check whether two given strings are anagram of each other or not.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different.
#
# For example, “abcd” and “dabc” are an anagram of each other.

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


test_str_1 = "abced"
test_str_2 = "abdtrfec"
result = is_anagram(test_str_1, test_str_2)
print(result)
#####################################################################################################################

# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
#
# The string will only contain lowercase characters a-z and it's not a palindrome.
# For exampole,
# “radkar” is almost a palindrome.
# “radario” is not almost a palindrome.

def is_almost_palindrome(s):
    for i in range(len(s)):
        current_str = s[:i] + s[i + 1:]
        if current_str == current_str[::-1]:
            return True
        else:
            return False

test_pos = "radkar"
test_neg = "rodario"
result_pal_pos = is_almost_palindrome(test_pos)
print(result_pal_pos)

result_pal_neg = is_almost_palindrome(test_neg)
print(test_neg)
