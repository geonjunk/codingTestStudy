from collections import deque
dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    if w == 1 and h == 1:
        arr = int(input())
        print(arr)
    else:
        ans = 0
        arr = [list(map(int, input().split())) for i in range(h)]
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1:
                    ans += 1
                    q = deque()
                    q.append((i, j))
                    arr[i][j] = 2
                    while q:
                        nowR, nowC = q.popleft()
                        for d in dir:
                            nextR, nextC = nowR+d[0], nowC+d[1]
                            if nextR < 0 or nextR >= h or nextC < 0 or nextC >= w:
                                continue
                            if arr[nextR][nextC] == 1:
                                arr[nextR][nextC] = 2
                                q.append((nextR, nextC))
        print(ans)

    # 0 - 바다, 1 - 땅
