n,m = map(int,input().split())
sr,sc,sd = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(r,c,d):
    arr[r][c] = 2
    for i in range(1,5):
        nextD = (d-i)%4
        nextR,nextC = r+dir[nextD][0],c+dir[nextD][1]
        if nextR<0 or nextR>=n or nextC<0 or nextC>=m:
            continue

        if arr[nextR][nextC]==0:
            dfs(nextR,nextC,nextD)
            return
    
    r,c = r-dir[d][0],c-dir[d][1]
    if arr[r][c]!=1:
        dfs(r,c,d)
dfs(sr,sc,sd)

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            ans+=1

print(ans)

