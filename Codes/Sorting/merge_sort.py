def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    # Step 1: Split the array into halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Step 2: Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10,54,2,7,6,3,5,23,4,12,34,5,89,34,75,345,23]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
