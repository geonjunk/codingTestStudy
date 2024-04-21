X = int(input())
dp = [[0, 0] for _ in range(X+1)]
dp[1] = [0, 0]

# (이전 수, 연산 횟수)
for i in range(2, X+1):
    dp[i] = [i-1, dp[i-1][1]+1]
    if i % 3 == 0 and dp[i][1] > dp[i//3][1]+1:
        dp[i][0] = i//3
        dp[i][1] = dp[i//3][1]+1
    if i % 2 == 0 and dp[i][1] > dp[i//2][1]+1:
        dp[i][0] = i//2
        dp[i][1] = dp[i//2][1]+1

print(dp[X][1])
while X > 0:
    print(X, end=" ")
    X = dp[X][0]
