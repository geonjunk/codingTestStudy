# 2. 삽입 정렬 - 하나씩 삽입하는 정렬 => 인접한 인덱스를 계속해서 비교해나간다, 보통 O(N^2), 거의 정렬되어있는경우 O(N)
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)
