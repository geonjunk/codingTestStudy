from collections import deque
n, k = map(int, input().split())

# 1. BFS
visited = [-1]*100001
q = deque()
q.append((n, 0))
visited[n] = 0
ansTime, ansCount = 1e9, 0
while q:
    now, t = q.popleft()
    if now == k:
        ansTime = t
        ansCount += 1
    else:
        for nextPos in [now*2, now+1, now-1]:
            if 0 <= nextPos <= 100000:
                if visited[nextPos] < 0 or visited[nextPos] == visited[now]+1:
                    visited[nextPos] = visited[now]+1
                    q.append((nextPos, t+1))

print(ansTime)
print(ansCount)
