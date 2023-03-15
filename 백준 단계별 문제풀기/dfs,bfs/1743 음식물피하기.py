from collections import deque
n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
trash = []

for i in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
    trash.append((r-1, c-1))
ans = 0
for (r, c) in trash:
    if arr[r][c] == 1:
        q = deque()
        size = 1
        q.append((r, c))
        arr[r][c] = 2
        while q:
            nowR, nowC = q.popleft()
            for d in dir:
                nextR, nextC = d[0]+nowR, d[1]+nowC
                if nextR < 0 or nextR >= n or nextC < 0 or nextC >= m:
                    continue
                if arr[nextR][nextC] == 1:
                    size += 1
                    q.append((nextR, nextC))
                    arr[nextR][nextC] = 2
        ans = max(ans, size)
print(ans)
