n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]
for i in range(1, n):
    if lis[len(lis)-1] < arr[i]:
        lis.append(arr[i])
    else:
        left = 0
        right = len(lis)-1
        while left <= right:
            mid = (left+right)//2
            if lis[mid] >= arr[i]:
                right = mid-1
            elif lis[mid] < arr[i]:
                left = mid+1
        lis[left] = arr[i]
print(len(lis))
