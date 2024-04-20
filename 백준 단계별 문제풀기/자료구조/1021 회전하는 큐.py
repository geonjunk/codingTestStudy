from collections import deque

n,m = map(int,input().split())
numbers = list(map(int,input().split()))
answer = 0

q = deque([i for i in range(1,n+1)])

for n in numbers:
    while True:
        idx = q.index(n)
        if idx ==0:
            q.popleft()
            break
        else:
            if idx<len(q)/2:
                while n != q[0]:
                    q.append(q.popleft())
                    answer+=1
            else:
                while n != q[0]:
                    q.appendleft(q.pop())
                    answer+=1
            
print(answer)
