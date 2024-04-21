import math
def solution(progresses, speeds):
    answer = []
    q = []
    for i in range(len(progresses)):
        w = 100-progresses[i]
        days = math.ceil(w /speeds[i]) 
        q.append(days)
        
    
    now = q[0]
    answer.append(0)
    for i in range(len(progresses)):
        if now>=q[i]:
            answer[-1]+=1
        else:
            now = q[i]
            answer.append(1)

    return answer