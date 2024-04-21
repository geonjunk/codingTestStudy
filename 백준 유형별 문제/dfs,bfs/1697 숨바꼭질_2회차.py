from collections import deque
n,k =map(int,input().split())
INF = 1e9
visited = [INF]*100001
q= deque()
q.append((n,0))
visited[n]=0
while q:
    now ,t = q.popleft()

    if now==k:
        break

    if visited[now]<t:
        continue
    
    for x in (now*2,now+1,now-1):
        if x>=0 and x<=100000 and t+1<visited[x]:
            visited[x]=t+1
            q.append((x,t+1))

print(visited[k])
