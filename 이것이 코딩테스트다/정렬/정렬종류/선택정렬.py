# 1. 선택 정렬 - 최솟값을 선택하여 정렬 계속 풀스캔 => O(N^2)
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)-1):
    minIdx = i
    for j in range(i+1, len(arr)):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)
