from collections import deque

n,m = map(int,input().split())
numbers = list(map(int,input().split()))
q = deque([i+1 for i in range(n)])

cnt = 0
for num in numbers:
    if num != q[0]:
        idx = q.index(num)
        if idx <len(q)/2:
            while q[0]!=num:
                cnt+=1
                q.append(q.popleft())
        else:
            while q[0]!=num:
                cnt+=1
                q.appendleft(q.pop())
    q.popleft()

print(cnt)