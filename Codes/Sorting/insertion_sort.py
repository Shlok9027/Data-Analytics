
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i -1

        while j >= 0  and  arr[j] > key :
            arr[j+1] = arr[j]

            j -= 1

        arr[j + 1] = key
    return arr

arr = [34,12,453,24,21,45,4,98,22,3,4,5,67,2,53,21,5,432,1,1,14,2,4,312]

print(insertion_sort(arr))
