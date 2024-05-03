n,m = map(int,input().split())
dir = [[] for _ in range(6)]

dir[1]=[[(0,1)],[(1,0)],[(0,-1)],[(-1,0)]]
dir[2] =[[(1,0),(-1,0)],[(0,1),(0,-1)]]
dir[3] = [[(1,0),(0,1)],[(1,0),(0,-1)],[(-1,0),(0,1)],[(-1,0),(0,-1)]]
dir[4] = [[(1,0),(0,1),(0,-1)],[(1,0),(0,1),(-1,0)],[(1,0),(-1,0),(0,-1)],[(0,-1),(-1,0),(0,1)]]
dir[5] = [[(0,1),(1,0),(0,-1),(-1,0)]]


arr = [list(map(int,input().split())) for _ in range(n)]
posArr = []
ans = 1e9

for i in range(n):
    for j in range(m):
        if arr[i][j]!=0 and arr[i][j]!=6:
            posArr.append((i,j,arr[i][j]))


def dfs(idx,graph):
    global ans
    if idx==len(posArr):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    cnt+=1
        ans = min(cnt,ans)
        return

    nowR,nowC,num = posArr[idx]
    for d in dir[num]:
        tmpGraph= [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                tmpGraph[i][j]=graph[i][j]
        for (r,c) in d:
            tmpR,tmpC = nowR,nowC
            while 0<=tmpR<n and 0<=tmpC<m:
                if tmpGraph[tmpR][tmpC]==6:
                    break
                elif tmpGraph[tmpR][tmpC]==0:
                    tmpGraph[tmpR][tmpC] = '#'
                tmpR+=r
                tmpC+=c
        dfs(idx+1,tmpGraph)
        tmpGraph=graph

dfs(0,arr)
print(ans)