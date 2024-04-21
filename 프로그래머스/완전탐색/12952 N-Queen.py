answer = 0
def solution(n):
    queens = [-1]*n
    def backtracking(cnt):
        global answer
        if cnt == n:
            answer+=1
            return 
        
        for i in range(n):
            if isPromising(cnt,i):
                queens[cnt]=i
                backtracking(cnt+1)
                queens[cnt]=-1
                
    def isPromising(r,c):
        for i in range(r):
            if queens[i]==c:
                return False
            if abs(r-i) == abs(c-queens[i]):
                return False
        return True
    
    backtracking(0)
    return answer
