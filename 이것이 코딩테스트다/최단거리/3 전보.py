import sys
import heapq

input = sys.stdin.readline
n, m, c = map(int, input().split())
INF = 1e9
dist = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# C에서 도착가능한곳들
dist[c] = 0
pq = []
heapq.heappush(pq, (0, c))

while pq:
    d, now = heapq.heappop(pq)
    if dist[now] < d:
        continue

    for i in graph[now]:
        cost = i[1]+dist[now]
        if cost < dist[i[0]]:
            dist[i[0]] = cost
            heapq.heappush(pq, (cost, i[0]))

ans1, ans2 = 0, 0
for d in dist:
    if d < INF and d != 0:
        ans1 += 1
        ans2 = max(d, ans2)
print(ans1, end=" ")
print(ans2)
