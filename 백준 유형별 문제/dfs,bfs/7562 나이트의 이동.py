from collections import deque
t = int(input())
dir = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
for _ in range(t):
    l = int(input())
    arr = [[0]*l for i in range(l)]
    startR, startC = map(int, input().split())
    destR, destC = map(int, input().split())
    arr[startR][startC] = 1
    q = deque()
    q.append((startR, startC))
    while q:
        nowR, nowC = q.popleft()
        if nowR == destR and nowC == destC:
            break
        for d in dir:
            nextR, nextC = nowR+d[0], nowC+d[1]
            if nextR < 0 or nextR >= l or nextC < 0 or nextC >= l:
                continue
            if arr[nextR][nextC] == 0:
                arr[nextR][nextC] = arr[nowR][nowC]+1
                q.append((nextR, nextC))
    print(arr[destR][destC]-1)
