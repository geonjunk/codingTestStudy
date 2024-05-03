from collections import deque

n,w,l = map(int,input().split())
trucks = list(map(int,input().split()))

q=[0]*w
q = deque(q)
now = 0
time = 0

while q:
    now-=q.popleft()
    time+=1

    if trucks:
        if now+trucks[0]<=l: # 들어갈 수 있음
            nowTruck = trucks.pop(0)
            q.append(nowTruck)
            now+=nowTruck
        else: # 들어갈 수 없음
            q.append(0)
  
print(time)

