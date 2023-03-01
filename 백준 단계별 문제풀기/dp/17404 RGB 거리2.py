n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# R -> G,B
# G -> R,B
# B -> R,G
ans = 1e9
for c in range(3):
    dp = [[0]*3 for _ in range(n)]  # R,G,B
    dp[0] = [1e9, 1e9, 1e9]
    dp[0][c] = arr[0][c]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2])+arr[i][0]  # R
        dp[i][1] = min(dp[i-1][0], dp[i-1][2])+arr[i][1]  # G
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])+arr[i][2]  # B
    dp[n-1][c] = 1e9
    ans = min(ans, min(dp[n-1]))

print(ans)
