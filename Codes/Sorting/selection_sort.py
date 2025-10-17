def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


def print_list(arr):
    for num in arr:
        print(num, end=" ")
    print()

nums  = [56,23,78,23,54,2,21]

print("before sorting : ")
print_list(nums)


selection_sort(nums)

print("after sorting : ")
print_list(nums)