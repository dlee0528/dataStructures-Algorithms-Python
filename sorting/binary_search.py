from util import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    for index, num in enumerate(numbers_list):
        if num == number_to_find:
            return index
    return False

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    middle_index = 0
    

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2 # get integer portion
        mid_number = numbers_list[middle_index]

        if mid_number == number_to_find:
            return middle_index
        
        if mid_number < number_to_find:
            left_index = middle_index
        else:
            right_index = middle_index

    return None


def binary_serach_recursive(numbers_list, number_to_find, left_index, right_index):
    if left_index > right_index:
        return False

    mid_index = (left_index + right_index) // 2

    if mid_index >= len(numbers_list) or mid_index < 0:
        return False

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index
    
    if mid_number < number_to_find:
        left_index = mid_index + 1
         
    else:
        right_index = mid_index - 1

    return binary_serach_recursive(numbers_list, number_to_find, left_index, right_index)



if __name__== "__main__":  
    numbers_list = [12,15,17,19,21,24,45,67]
    number_to_find = 24

    index = linear_search(numbers_list, number_to_find)
    print(f"Lineary Search Result: Number {number_to_find} found at index {index}")
    
    index = binary_search(numbers_list, number_to_find)
    print(f"Binary Search (Iterative) Result: Number {number_to_find} found at index {index}")
    
    index = binary_serach_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Binary Search (Recursive) Result: Number {number_to_find} found at index {index}")