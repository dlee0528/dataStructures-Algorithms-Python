def insertion_sort(elements):
    # assume first element is part of a sorted array
    # left is sorted and compare it with current element
    for i in range(1, len(elements)):
        anchor = elements[i]

        j = i -1

        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        
        elements[j+1] = anchor
    

if __name__ == "__main__":
    elements = [5,9,2,1,67,34,88,34]
    insertion_sort(elements)
    print(elements)