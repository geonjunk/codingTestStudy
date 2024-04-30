n, m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
dir = [(0,0),(0,1),(1,0),(1,1)]
ans = 1
for i in range(n):
    for j in range(m):
        pos = [[i,j] for _ in range(4)]
        flag = True
        while flag:
            for k in range(1,len(dir)):
                pos[k]=[pos[k][0]+dir[k][0],pos[k][1]+dir[k][1]]
                if pos[k][0]>=n or pos[k][1]>=m:
                    flag = False
                    break
            if flag:
                now = arr[pos[0][0]][pos[0][1]]
                ansFlag = True
                for k in range(1,4):
                    if now!=arr[pos[k][0]][pos[k][1]]:
                        ansFlag=False
                        break
                if ansFlag:
                    l = abs(pos[0][0]-pos[3][0])+1
                    ans = max(ans,l*l)

print(ans)

