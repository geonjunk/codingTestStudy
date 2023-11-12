n,m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
chickens =[]
houses =[]
answer = 1e9


def calChickenLength(result):
    ans =0
    for h in houses:
        way = 1e9
        for r in result:
            way =min (abs(r[0]-h[0])+abs(r[1]-h[1]),way)
        ans+=way
    return ans

def dfs(result,idx):
    global answer
    if len(result)==m:
        answer = min(calChickenLength(result),answer)
        return
    
    for i in range(idx,len(chickens)):
        result.append(chickens[i])
        dfs(result,i+1)
        result.pop()

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            houses.append((i,j))
        if arr[i][j]==2:
            chickens.append((i,j))

result =[]
dfs(result,0)

print(answer)
