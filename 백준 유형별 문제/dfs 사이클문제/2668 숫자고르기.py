n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

visited = [False]*(n+1)
ans = []


def dfs(now):
    global ans, cycle
    visited[now] = True
    cycle.append(now)

    if not visited[arr[now]]:
        dfs(arr[now])
    elif arr[now] in cycle:
        nxt = arr[now]
        result = [now]
        while nxt != now:
            result.append(nxt)
            nxt = arr[nxt]
        ans += result


for i in range(1, n+1):
    if not visited[i]:
        cycle = []
        dfs(i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
