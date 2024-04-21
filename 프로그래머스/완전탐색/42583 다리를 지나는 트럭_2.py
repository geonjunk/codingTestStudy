from collections import deque 
def solution(bridge_length, weight, truck_weights):
    answer = 0
    now_w = 0 
    bridge = [0]*bridge_length
    bridge = deque(bridge)
    
    while bridge:
        answer+=1
        now_w -= bridge.popleft()
        
        if truck_weights:
            if now_w+truck_weights[0]<=weight:
                now = truck_weights.pop(0)
                bridge.append(now)
                now_w+=now
            else:
                bridge.append(0)
    
    return answer

