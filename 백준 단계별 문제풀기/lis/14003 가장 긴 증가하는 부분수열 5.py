n = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]
pos = [(len(lis)-1, arr[0])]
for i in range(1, n):
    if lis[len(lis)-1] < arr[i]:
        lis.append(arr[i])
        pos.append((len(lis)-1, arr[i]))
    else:
        left = 0
        right = len(lis)-1
        while left <= right:
            mid = (left+right)//2
            if lis[mid] >= arr[i]:
                right = mid-1
            else:
                left = mid+1

        lis[left] = arr[i]
        pos.append((left, arr[i]))

print(len(lis))
now = len(lis)-1
ans = []
for i in range(len(pos)-1, -1, -1):
    if pos[i][0] == now:
        ans.append(pos[i][1])
        now -= 1
for i in ans[::-1]:
    print(i, end=" ")
