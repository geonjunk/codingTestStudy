c,r = map(int,input().split())
arr= [ [False]*c for _ in range(r)]

seq = int(input())
if seq>(r*c):
    print(0)
else:
    dir = [(-1,0),(0,1),(1,0),(0,-1)]

    nextR,nextC,idx = r-1,0,0
    for i in range(seq):
        nowR,nowC = nextR,nextC
        arr[nowR][nowC]=True

        for i in range(4):
            nextR,nextC = nowR+dir[idx][0],nowC+dir[idx][1]
            if nextR>=0 and nextR<r and nextC>=0 and nextC<c and not arr[nextR][nextC]:
                break
            else:
                idx=(idx+1)%4

    print(nowC+1,r-nowR)

