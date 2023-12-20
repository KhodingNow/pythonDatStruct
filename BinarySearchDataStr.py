# Binary = [1,4,5,7,80,8,9] ..think of MEDian in Stats
# look for 1/2 point location, if target < half point, dicard the other
# half and only search one other half only

# start with  ITERATIVE BINARY SEARCH

def binary_itr(arr, start, end, target):
    while start <= end:

        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return start


arr = [1, 4, 5, 7, 80, 8, 9]
target = 8

result = binary_itr(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element is present at index {result}")

    # print("Element is present at index %d" % result)
else:
    print(f"Element is present at index {arr}")

    # print("Element is not present in array")
