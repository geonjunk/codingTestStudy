n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(r, c):
    if r == n-1 and c == m-1:
        return 1

    if dp[r][c] == -1:
        dp[r][c] = 0

        for d in dir:
            nextR, nextC = r+d[0], c+d[1]
            if nextR < 0 or nextR >= n or nextC < 0 or nextC >= m:
                continue
            if arr[nextR][nextC] < arr[r][c]:
                dp[r][c] += dfs(nextR, nextC)

    return dp[r][c]


dfs(0, 0)

print(dfs(0, 0))
