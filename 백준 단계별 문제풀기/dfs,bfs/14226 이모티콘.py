from collections import deque
s = int(input())

q = deque()
q.append((0, 1, 0))
dp = [[1e9]*1001 for _ in range(1001)]
dp[0][1] = 0
while q:
    clipBoard, now, sec = q.popleft()
    if now == s:
        print(sec)
        break
    if dp[now][now] > sec+1:
        dp[now][now] = sec+1
        q.append((now, now, sec+1))  # 복사
    if clipBoard+now <= 1000 and dp[clipBoard][clipBoard+now] > sec+1:
        dp[clipBoard][clipBoard+now] = sec+1
        q.append((clipBoard, now+clipBoard, sec+1))
    if now > 1 and dp[clipBoard][now-1] > sec+1:
        dp[clipBoard][now-1] = sec+1
        q.append((clipBoard, now-1, sec+1))

    # 1. 복사
    # 2. 붙여놓기
    # 3. 하나 삭제
