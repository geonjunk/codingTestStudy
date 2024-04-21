n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False]*n
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0


def backtracking(now, count):
    global ans
    if count == 5:
        ans = 1
        return

    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            backtracking(i, count+1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    backtracking(i, 1)
    visited[i] = False

print(ans)
