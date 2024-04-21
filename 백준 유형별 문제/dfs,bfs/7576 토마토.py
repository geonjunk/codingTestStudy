from collections import deque
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque()
zeroCount = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
        if arr[i][j] == 0:
            zeroCount += 1

while q:
    nowR, nowC = q.popleft()

    for d in dir:
        nextR, nextC = d[0]+nowR, d[1]+nowC

        if nextR < 0 or nextR >= n or nextC < 0 or nextC >= m:
            continue

        if arr[nextR][nextC] == 0:
            arr[nextR][nextC] = arr[nowR][nowC]+1
            q.append((nextR, nextC))
            zeroCount -= 1

ans = -1
if zeroCount == 0:
    for i in range(n):
        ans = max(ans, max(arr[i])-1)

print(ans)
