import heapq
n, m = map(int,input().split()) # 정점, 간선
graph = [[] for _ in range(n+1)]
dist = [1e9] *(n+1)

for i in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))
dist[1]=0
pq = []
heapq.heappush(pq,(0,1))

while pq:
    w,now =heapq.heappop(pq)
    if dist[now]<w:
        continue

    for g in graph[now]:
        nextPos,nextW = g
        if dist[nextPos]>dist[now]+nextW:
            dist[nextPos]=dist[now]+nextW
            heapq.heappush(pq,(dist[nextPos],nextPos))

print(dist[n])    




"""
각점에서 최단거리 
"""
