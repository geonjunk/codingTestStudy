arr = [list(map(int,input().split())) for _ in range(19)]

dir = [(0,1),(1,0),(1,1),(-1,1)]

answerFlag =False

for i in range(19):
    for j in range(19):
        now = arr[i][j]
        if now!=0:
            for d in dir:
                cnt = 1
                nRow = d[0]+i
                nCol = d[1]+j
                while 0<=nRow<19 and 0<=nCol<19 and arr[nRow][nCol]==now:
                    cnt+=1
                    if cnt==5:
                        if 0<=i-d[0]<19 and 0<=j-d[1]<19 and arr[i-d[0]][j-d[1]]==now:
                            break
                        if 0<=nRow+d[0]<19 and 0<=nCol+d[1]<19 and arr[nRow+d[0]][nCol+d[1]]==now:
                            break
                        answerFlag = True
                        print(now)
                        print(i+1,j+1)
                        break
                    nRow+=d[0]
                    nCol+=d[1]
    if answerFlag:
        break

if not answerFlag:
    print(0)
