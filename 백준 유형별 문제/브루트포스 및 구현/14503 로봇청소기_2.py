n,m = map(int,input().split())
nowR,nowC,nowD = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
dir = [(-1,0),(0,1),(1,0),(0,-1)]

cnt = 0
while True:
    if arr[nowR][nowC]==0:
        arr[nowR][nowC]=2
        cnt+=1
        
    shiftFlag = False
    for i in range(4):
        nowD=(nowD-1)%4
        nextR,nextC = nowR + dir[nowD][0],nowC + dir[nowD][1]
        if arr[nextR][nextC]==0:
            nowR = nextR
            nowC = nextC
            shiftFlag = True
            break
        

    if not shiftFlag:
        nowR -=dir[nowD][0]
        nowC -=dir[nowD][1]

        if arr[nowR][nowC]==1:
            break

print(cnt)
