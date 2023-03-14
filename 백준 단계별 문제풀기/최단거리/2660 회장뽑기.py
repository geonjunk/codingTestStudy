n = int(input())
INF = 1e9
dist = [[INF]*(n+1) for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1
    if a == -1 and b == -1:
        break
for i in range(1, n+1):
    dist[i][i] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

point = [0]*(n+1)
point[0] = INF
for i in range(1, n+1):
    for j in range(1, n+1):
        point[i] = max(point[i], dist[i][j])

minPoint = min(point)
count = 0
result = []
for i in range(1, n+1):
    if point[i] == minPoint:
        result.append(i)
        count += 1

print(minPoint, count)
for i in result:
    print(i, end=" ")
# 회장 후보의 점수와 후보의수
# 회장 후보 오름차순

# 1. floyd warshall로 모든길이 구한뒤 -> 각 길이의 최대값을 점수로함
