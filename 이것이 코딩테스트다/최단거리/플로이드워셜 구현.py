import heapq

INF = 1e9
n, m = map(int, input().split())  # 노드, 간선(버텍스)
start = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

pq = []
heapq.heappush(pq, (0, start))
dist[start] = 0
while pq:  # 더이상 갈곳이없을때
    d, now = heapq.heappop(pq)

    if dist[now] < d:  # 이미처리된 노드면 (visited 대신 이걸로 판단, flag 사용해도됨)
        continue

    for i in graph[now]:
        cost = d+i[1]
        if cost < dist[i[0]]:
            dist[i[0]] = cost
            heapq.heappush(pq, (cost, i[0]))

print(dist[1:])
