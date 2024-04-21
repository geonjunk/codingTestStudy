import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
virus =[]
answer =0
for i in range(n):
    for j in range(m):
        if arr[i][j] ==2:
            virus.append((i,j))

def setWall(arr,cnt):
    if cnt ==3:
        calSafeZones(arr)
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][j]=1
                setWall(arr,cnt+1)
                arr[i][j]=0


def calSafeZones(arr):
    global answer
    tmpArr =[[0]*m for _ in range(n)]
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    q = deque(virus)
    
    for i in range(n):
        for j in range(m):
            tmpArr[i][j] = arr[i][j]
               

    while q:
        nowR,nowC = q.popleft()
        for d in dir:
            nextR = nowR+d[0]
            nextC = nowC+d[1]
            if nextR<0 or nextR>=n or nextC<0 or nextC>=m:
                continue
            if tmpArr[nextR][nextC]==0:
                tmpArr[nextR][nextC]=2
                q.append((nextR,nextC))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmpArr[i][j]==0:
                cnt+=1

    answer = max(cnt,answer)
  
setWall(arr,0)
print(answer)