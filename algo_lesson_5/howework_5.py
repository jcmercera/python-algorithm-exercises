# 1 Implement the selection sort algorithm that is sorting in descending order.

def selection_sort_descending(arr):
    for i in range(len(arr)):
        min_num = i
        for number in range(i + 1, len(arr)):
            if arr[min_num] < arr[number]:
                min_num = number
            # swap
            arr[i], arr[min_num] = arr[min_num], arr[i]
            # main
    return arr


test_arr = [2, 5, 7, 9, 11, 56, 90, 54, 89, 100]
results = selection_sort_descending(test_arr)
print('Selection sort in descending order:', results)


# 2 Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort_descending(arr):
    for i in range(len(arr)):
        for number in range(0, len(arr) - i - 1):
            if arr[number] < arr[number + 1]:
                (arr[number], arr[number + 1]) = (arr[number + 1], arr[number])

    return arr


test_bubble = [3, 71, 86, 33, 76, 46, 93, 20, 65]
results_2 = bubble_sort_descending(test_bubble)
print('Bubble sort in descending order:', results_2)


# 3 Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

def insertion_sort(arr_3):
    for i in range(1, len(arr_3)):
        key = arr_3[i]
        j = i - 1
        while j >= 0 and key > arr_3[j]:
            arr_3[j + 1] = arr_3[j]
            j = j - 1
        arr_3[j + 1] = key
    return arr_3


test_insertion = [87, 9, -34, -49, 65]
results_3 = insertion_sort(test_insertion)
print('Insertion sort in descending Order:', results_3)


# 4 Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.
###### I FOLLOWED THE STEPS FROM THE CLASS RECORDING BUT I HONESLTY DON'T KNOW WHAT I DID ################

def merge_sort(arr_4):
    if len(arr_4) <= 1:
        return arr_4

    middle = len(arr_4) // 2
    return merge_arrays(merge_sort(arr_4[:middle]), merge_sort(arr_4[middle:]))


def merge_arrays(left_arr, right_arr):
    merged_list = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_list.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_list.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_list.append(left_arr[i])
            i += 1
        else:
            merged_list.append(right_arr[j])
            j += 1
    return merged_list


test_merge = [19, 43, 23, 61, 26, 72, 65]
result_4 = merge_sort(test_merge)
print('Merged sort:', result_4)
