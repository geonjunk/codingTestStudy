n = int(input())
arr =[]
answer = 0

for i in range(n):
    t,p = map(int,input().split())
    arr.append((t,p))
def dfs(now,p):
    global answer
    answer = max(answer,p)
    for i in range(now,n):
        if i+arr[i][0]<=n:
            dfs(i+arr[i][0],p+arr[i][1])
        
dfs(0,0)

print(answer)



