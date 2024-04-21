def solution(bridge_length, weight, truck_weights):
    answer = 0
    now = [] 
    nowSum = 0 
    destCnt = 0 
    trucksLen = len(truck_weights)
    while destCnt < trucksLen:
        answer+=1
        for i in range(len(now)):
            now[i][0]-=1
            
        if now and now[0][0]<=0:
            outTruck = now.pop(0)
            nowSum-=outTruck[1]
            destCnt+=1
            
        if truck_weights and nowSum+truck_weights[0]<=weight:
            nowSum+=truck_weights[0]
            now.append([bridge_length,truck_weights[0]])
            truck_weights.pop(0)

    return answer