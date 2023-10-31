n, m = map(int, input().split())
# 최소한의 화폐수
coin = []
dp = [1e9]*(10001)
for i in range(n):
    now = int(input())
    coin.append(now)
    dp[now] = 1

for i in range(1, m+1):
    for c in coin:
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[m] == 1e9:
    print(-1)
else:
    print(dp[m])
