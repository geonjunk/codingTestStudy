n = int(input())
# 2xn을 채우는 경우의 수
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    dp[i] = (dp[i-1]+dp[i-2]*2) % 796796  # 작은것 하나더 세우는건 이미 고려
print(dp[n])
