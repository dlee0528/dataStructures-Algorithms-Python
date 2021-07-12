def selection_sort(elements):
    size = len(elements)

    for i in range(size-1):
        for j in range(i, size):
            if elements[i] <= elements[j]:
                elements[i] = elements[i]

        
    

if __name__ == "__main__":
    elements = [5,9,2,1,67,34,88,34]
    selection_sort(elements)
    print(elements)