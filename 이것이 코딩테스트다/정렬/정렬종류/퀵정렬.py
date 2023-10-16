# 4. quick sort => 피벗을 정하여 피벗을 경계로 비교를 해나가며 정렬을 재귀적으로 하는방식 , O(NlogN)
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quickSort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1

        while right > start and arr[pivot] <= arr[right]:
            right -= 1

        if left > right:  # 작은곳이므로 right 가맞음
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quickSort(arr, start, left-1)
    quickSort(arr, left+1, end)


quickSort(arr, 0, len(arr)-1)
print(arr)
