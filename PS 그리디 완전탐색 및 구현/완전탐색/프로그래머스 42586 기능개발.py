from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        
        cnt = 0
        for i in range(len(progresses)):
            now = progresses.popleft()
            if now>=100:
                cnt+=1
                speeds.popleft()
            else:
                progresses.appendleft(now)
                break
        if cnt>0:
            answer.append(cnt)
    
    return answer