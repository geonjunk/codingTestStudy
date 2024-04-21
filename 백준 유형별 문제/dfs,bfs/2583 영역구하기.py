from collections import deque
m,n,k = map(int,input().split())

arr = [[0]*n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())

    for x in range(x1,x2):
        for y in range(y1,y2):
            arr[y][x] = 1


def bfs(i,j):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    q= deque()
    cnt = 1
    q.append((i,j))
    arr[i][j] = 1
    while q:
        nowY,nowX = q.popleft()

        for d in dir:
            nextY,nextX = nowY+d[0],nowX + d[1]

            if nextY<0 or nextY>=m or nextX<0 or nextX>=n:
                continue
            
            if arr[nextY][nextX]==0:
                q.append((nextY,nextX))
                arr[nextY][nextX]= 1
                cnt+=1

    return cnt

answer = []
for i in range(m):
    for j in range(n):
        if arr[i][j] ==0:
            answer.append(bfs(i,j))
answer.sort()

print(len(answer))
for a in answer:
    print(a,end=" ")
print()
