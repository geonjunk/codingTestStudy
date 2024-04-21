from collections import deque

def bfs(x,arr,n):
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    q= deque()
    visited = [[False]*n for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j]>x:
                q.append((i,j)) 
                visited[i][j]=True
                while q:
                    nowR,nowC = q.popleft()

                    for d in dir:
                        nextR, nextC = nowR+d[0],nowC+d[1]

                        if nextR<0 or nextR>=n or nextC<0 or nextC>=n:
                            continue

                        if arr[nextR][nextC]>x and not visited[nextR][nextC]:
                            q.append((nextR,nextC))
                            visited[nextR][nextC]=True
                answer+=1
    return answer

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
minHeight,maxHeight = 1e9,0

answer = 1 

for i in range(n):
    for j in range(n):
        minHeight=min(minHeight,arr[i][j])
        maxHeight=max(maxHeight,arr[i][j])

for x in range(minHeight,maxHeight):
    answer = max(bfs(x,arr,n),answer)

print(answer)
    
