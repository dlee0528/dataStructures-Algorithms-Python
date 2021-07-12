def swap(arr, a,b):
    arr[a], arr[b] = arr[b], arr[a]     

def partition(elements, left, right):
    pivot = elements[(left + right) // 2] # pick pivot point
    
    while(left <= right):
        # find element on left that should be on right
        while(elements[left] < pivot):
            left += 1
        
        # find element n right that should be on left
        while(elements[right] > pivot):
            right -= 1

        # swap elements, and move left and right iindicies
        if(left <= right):
            swap(elements, left, right)
            left += 1
            right -= 1

    return left

# nlogn
def quick_sort(elements, left, right):
    index = partition(elements, left, right)
    if(left < index - 1): # sort left half
        quick_sort(elements, left, index - 1)
    
    if(index < right): # sort right half
        quick_sort(elements, index, right)


if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements, 0, len(elements) -1)
    print(elements)