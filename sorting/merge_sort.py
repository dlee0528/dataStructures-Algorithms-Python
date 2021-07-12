# O(nlongn)
# merge: O(n)
# sorting: O(logn)
def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left) # sort the first half
        merge_sort(right) # sort the second half

        i = j = k = 0

        # copy data to temp arrays left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1

            k += 1

        
        # checking if any element was left
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        # checking if any element was left 
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    a=[5,8,12,56,89, 100]
    merge_sort(a)
    print(a)
    