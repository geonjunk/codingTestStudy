from collections import deque
f, s, g, u, d = map(int, input().split())
q = deque()
visited = [-1]*(f+1)
visited[s] = 0
q.append(s)

while q:
    now = q.popleft()
    if now == g:
        break
    if now+u <= f and visited[now+u] < 0:
        q.append(now+u)
        visited[now+u] = visited[now]+1
    if now-d > 0 and visited[now-d] < 0:
        q.append(now-d)
        visited[now-d] = visited[now]+1

if visited[g] < 0:
    print("use the stairs")
else:
    print(visited[g])
