from statistics import mean


# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical
# mean. The arithmetical mean is the sum of all elements divided by the number of elements. Example: [1, 3, 5, 6, 4,
# 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]


def below_arithmetical_mean_list(arr):
    arithmetical_mean = mean(arr)
    new_list = []

    for n in arr:
        if n < arithmetical_mean:
            new_list.append(n)

    return new_list


test_arr = [10, 3, 42, 2, 6, 1]
result = below_arithmetical_mean_list(test_arr)
print('Below arithmetical mean list:', result)


# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.

def lowest_elements(list):
    sorted_list = list.sort()
    min1 = list[0]
    min2 = list[1]

    for i in range(2, len(list)):
        return min1, min2


test_array = [873637, 9883, 709836, 909383, 6253787]
result_lowest = lowest_elements(test_array)
print('Two lowerst numbers:', result_lowest)
