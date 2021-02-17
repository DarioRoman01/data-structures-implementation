"""Binary search implemntation."""

# decorartors
from algorithms.utils import time_it

@time_it
def linear_search(elements, val_to_find):
    for index, element in enumerate(elements):
        if element == val_to_find:
            return index
    
    return -1

@time_it
def binary_search(elements, val_to_find):
    left_index = 0
    right_index = len(elements) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = elements[mid_index]

        if mid_number == val_to_find:
            return mid_index
        elif mid_number < val_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

@time_it
def find_all_ocurrences(elements, val_find):
    index = binary_search(elements, val_find)
    indexes = [index]

    # find indexes in left side
    left_index = index - 1
    while left_index > 0:
        if elements[left_index] == val_find:
            indexes.append(left_index)
        
        left_index -= 1

    # find indexes in right side
    right_index = index + 1
    while right_index < len(elements) - 1:
        if elements[right_index] == val_find:
            indexes.append(right_index)

        right_index += 1

    return sorted(indexes)


def recursive_binary_search(elements, val_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = elements[mid_index]

    if mid_number == val_to_find:
        return mid_index

    elif mid_number < val_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return recursive_binary_search(elements, val_to_find, left_index, right_index)



if __name__ == "__main__":
    # Find index of all the occurances of a number from sorted list
    # This should return 5,6,7 as indices containing number 15 in the array
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    indexs = find_all_ocurrences(numbers, 15)
    print(f'Number found at {indexs} using linear search')


    # When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
    # number_list = [1,4,6,9,10,5,7]
    # number_to_find = 5

    # index = binary_search(number_list, number_to_find)
    # print(f'Number found at {index} using linear search')

    # because the list is not ordered, then when the program verifies that the value in the middle index
    #  of the list is greater than the value that is sought, it reduces the list to the left