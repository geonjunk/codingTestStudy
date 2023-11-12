import heapq

n,m,k,x = map(int,input().split())
graph=[[] for _ in range(n+1)]
result = [1e9] *(n+1)
for i in range(m):
    r,c = map(int,input().split())
    graph[r].append((c,1))

result[x] = 0
q=[]
heapq.heappush(q,(0,x))

while q:
    w,now = heapq.heappop(q)

    if result[now]<w:
        continue 

    for next in graph[now]:
        if result[next[0]]>result[now]+next[1]:
            result[next[0]]=result[now] +next[1]
            heapq.heappush(q,(result[next[0]],next[0]))


answer =[i for i in range(len(result)) if result[i]==k ]

if len(answer)==0:
    print(-1)
else:
    for a in answer:
        print(a)