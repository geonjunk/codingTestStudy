n = int(input())

queens = [-1]*n
answer = 0

def dfs(cnt):
    global answer
    if cnt == n:
        answer+=1
        return
    
    for now in range(n):
        if isPossible(cnt,now):
            queens[cnt]= now
            dfs(cnt+1)
            queens[cnt]= -1

def isPossible(cnt,now):
    for i in range(cnt):
        if queens[i]== now:
            return False
        if abs(now-queens[i]) == abs(cnt-i):
            return False
    return True

dfs(0)
print(answer)
