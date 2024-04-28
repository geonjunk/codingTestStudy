n = int(input())
arr = list(map(int,input().split()))

pos = -1

for i in range(n-1,0,-1):
    if arr[i]>arr[i-1]:
        pos = i-1
        break

if pos == -1:
    print(-1)
else:
    for i in range(n-1,pos,-1):
        if arr[pos] < arr[i]:
            arr[pos],arr[i] = arr[i],arr[pos]
            break
    arr = arr[:pos+1] +sorted(arr[pos+1:])
    for i in range(n):
        print(arr[i],end=" ")
    print()