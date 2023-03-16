T = int(input())


def dfs(now):
    global cycle, ans
    visited[now] = True
    cycle.append(now)

    if not visited[graph[now]]:
        dfs(graph[now])
    elif graph[now] in cycle:
        nxt = graph[now]
        ans += 1
        while nxt != now:
            ans += 1
            nxt = graph[nxt]


for _ in range(T):
    n = int(input())
    graph = [0]
    graph.extend(map(int, input().split()))
    ans = 0
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-ans)

"""

1->3
2->1
3->3
4->7
5->3
6->4
7->6

1. 사이클인경우 

"""
