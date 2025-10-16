# def bubbleSort(arr):
#     n = len(arr)

#     for i in range(n):
#         swapped = False

#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True

#         if  not swapped:
#             break

# arr = [3,2,5,2,9,7]
# bubbleSort(arr)
# print(arr)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

                swapped = True

        if (swapped == False):
            break

arr = [23,54,12,67,1,45,2,65,2,23,4,2,62,8,54]

bubble_sort(arr)
print(arr)