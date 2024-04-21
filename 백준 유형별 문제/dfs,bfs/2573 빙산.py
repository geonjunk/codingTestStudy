from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dir = [(0,1),(1,0),(0,-1),(-1,0)]
t = 0

# 영역 판별
def bfs(r,c,visited):
    q =deque()
    q.append((r,c))
    while q:
        nowR,nowC = q.popleft()

        if visited[nowR][nowC]:
            continue

        visited[nowR][nowC]=True
        for d in dir:
            nextR,nextC =d[0]+nowR,d[1]+nowC
            if nextR<0 or nextR>=n or nextC<0 or nextC>=m:
                continue
            if not visited[nextR][nextC] and arr[nextR][nextC]!=0:
                q.append((nextR,nextC))

# 현재상태 체크 
def check():
    cnt = 0
    visited=[[False]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if arr[r][c]!=0 and not visited[r][c]:
                bfs(r,c,visited)
                cnt+=1
    return cnt

def melting(arr):
    tmpArr =[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmpArr[i][j]=arr[i][j]

    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                nowR,nowC = i,j
                for d in dir:
                    r,c = nowR+d[0],nowC+d[1]
                    if r<0 or r>=n or c<0 or c>=m:
                        continue
                    if arr[r][c] ==0 and tmpArr[nowR][nowC]>0:
                        tmpArr[nowR][nowC]-=1
    for i in range(n):
        for j in range(m):
            arr[i][j] = tmpArr[i][j]


while True:
    now = check()
    if now!=1:
        if now==0:
            print(0)
        else:
            print(t)
        break
    
    melting(arr)
    t+=1

