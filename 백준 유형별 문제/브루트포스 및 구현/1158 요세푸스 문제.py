n,k = map(int,input().split())

arr = [i+1 for i in range(n)]
nowPos=0
result = []
while arr:
    nowPos = (nowPos+k-1)%len(arr)
    result.append(arr[nowPos])
    arr.pop(nowPos)

print("<",end="")
for i in range(len(result)):
    print(result[i],end="")
    if i!=len(result)-1:
        print(", ",end="")
print(">")