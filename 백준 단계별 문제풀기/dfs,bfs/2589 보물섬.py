from collections import deque

r, c = map(int, input().split())
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
arr = [list(input()) for _ in range(r)]
ans = -1
for i in range(r):
    for j in range(c):
        if arr[i][j] == "L":
            count = [[-1]*c for _ in range(r)]
            q = deque()
            q.append((i, j))
            count[i][j] = 0
            while q:
                nowR, nowC = q.popleft()
                ans = max(ans, count[nowR][nowC])
                for d in dir:
                    nextR, nextC = nowR+d[0], nowC+d[1]
                    if nextR < 0 or nextR >= r or nextC < 0 or nextC >= c:
                        continue
                    if count[nextR][nextC] == 0 and arr[nextR][nextC] == "L":
                        count[nextR][nextC] = count[nowR][nowC]+1
                        q.append((nextR, nextC))

print(ans)
