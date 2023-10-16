# 3. merge sort -> 재귀에는 종료조건이 있어야함!!
# 재귀적으로 반으로 나눈후 합병하며 정렬하는 방식 => O(NlogN)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def mergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left+right)//2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    i = left
    j = mid+1

    sortArr = []
    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            sortArr.append(arr[j])
            j += 1
        elif arr[i] == arr[j]:
            sortArr.append(arr[i])
            sortArr.append(arr[j])
            i += 1
            j += 1
        else:
            sortArr.append(arr[i])
            i += 1

    # 남아있는 값들 일괄 복사
    while i <= mid:
        sortArr.append(arr[i])
        i += 1

    while j <= right:
        sortArr.append(arr[j])
        j += 1

    for i in range(left, right+1):
        arr[i] = sortArr[i-left]


mergeSort(arr, 0, len(arr)-1)
print(arr)
