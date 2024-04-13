N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
INF = 1e9

for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
            graph[i][j] = INF



for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j]>=INF:
            print(0,end=" ")
        elif graph[i][j]>0:
            print(1,end=" ")
    print()
