n, d = map(int, input().split())
ways = []
visited = [i for i in range(d+1)]
for i in range(n):
    start, end, length = map(int, input().split())
    if end <= d:
        ways.append((start, end, length))
for i in range(d+1):
    if i > 0:
        visited[i] = min(visited[i-1]+1, visited[i])
    for w in ways:
        if w[0] == i and visited[i]+w[2] < visited[w[1]]:
            visited[w[1]] = visited[i]+w[2]
print(visited[d])
"""
1. 다익스트라로 
2. dp로 dp[n]=min(dp[n-1]+1,dp[n-1]
"""
