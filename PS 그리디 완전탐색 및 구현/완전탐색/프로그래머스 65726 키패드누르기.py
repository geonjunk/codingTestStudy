def solution(numbers, hand):
    answer = ''
    left,right = 10,12
    leftSet = set([1,4,7])
    rightSet = set([3,6,9])
    for n in numbers:
        if n in leftSet:
            left = n
            answer+="L"
        elif n in rightSet:
            right = n 
            answer+="R"
        else:
            if n == 0:
                n = 11
    
            nPos = ((n-1)//3,(n-1)%3)
            leftPos = ((left-1)//3,(left-1)%3)
            rightPos = ((right-1)//3,(right-1)%3)
            
            leftLength = abs(nPos[0]-leftPos[0])+abs(nPos[1]-leftPos[1])
            rightLength = abs(nPos[0]-rightPos[0])+abs(nPos[1]-rightPos[1])
            if leftLength>rightLength:
                right = n
                answer+="R"
            elif leftLength<rightLength:
                left = n
                answer+="L"
            else:
                if hand=="right":
                    right = n
                    answer+="R"
                else:
                    left = n
                    answer+="L"

    return answer
