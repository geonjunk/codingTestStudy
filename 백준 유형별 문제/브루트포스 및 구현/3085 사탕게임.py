n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0
dir = [(0,1),(1,0),(0,-1),(-1,0)]

def check():
    global answer
    for i in range(n):
        now = arr[i][0]
        cnt = 1

        for j in range(1,n):
            if now==arr[i][j]:
                cnt+=1
            else:
                now = arr[i][j]
                cnt=1
                
            answer = max(answer,cnt)
        
        now = arr[0][i]
        cnt = 1

        for j in range(1,n):
            if now==arr[j][i]:
                cnt+=1
            else:
                now = arr[j][i]
                cnt=1

            answer = max(answer,cnt)

for i in range(n):
    for j in range(n):
        now = arr[i][j]
        for d in dir:
            nextR,nextC = i+d[0],j+d[1]
            if nextR<0 or nextR>=n or nextC<0 or nextC>=n:
                continue
            if now!=arr[nextR][nextC]:
                arr[i][j],arr[nextR][nextC] = arr[nextR][nextC],arr[i][j]
                check()
                arr[i][j],arr[nextR][nextC] = arr[nextR][nextC],arr[i][j]

print(answer)
