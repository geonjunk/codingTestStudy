from collections import deque
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = [[0]*m for _ in range(n)]
q = deque()
count[0][0] = 1
q.append((0, 0))
while q:
    nowR, nowC = q.popleft()

    for d in dir:
        nextR, nextC = d[0]+nowR, d[1]+nowC
        if nextR < 0 or nextR >= n or nextC < 0 or nextC >= m:
            continue
        if arr[nextR][nextC] == '1' and count[nextR][nextC] == 0:
            count[nextR][nextC] = count[nowR][nowC]+1
            q.append((nextR, nextC))


print(count[n-1][m-1])
