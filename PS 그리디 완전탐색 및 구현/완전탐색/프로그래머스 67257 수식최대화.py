from collections import deque 
answer = 0
def solution(expression):
    global answer
    opRanks=[]

    dfs(opRanks,expression)
    
    return answer

def dfs(opRanks,expression):
    global answer
    
    if len(opRanks)==3:
        expressionArr = deque()
        now = ""
        for e in expression:
            if e in ["+","-","*"]:
                expressionArr.append(int(now))
                expressionArr.append(e)
                now=""
            else:
                now+=e
        expressionArr.append(int(now))
        
        
        for op in opRanks:
            stack = deque()
            while expressionArr:
                now = expressionArr.popleft()
                if now == op:
                    if op == "-":
                        result = stack.pop()-expressionArr.popleft()
                        stack.append(result)
                    if op == "+":
                        result = stack.pop()+expressionArr.popleft()
                        stack.append(result)
                    if op == "*":
                        result = stack.pop()*expressionArr.popleft()
                        stack.append(result)
                else:
                    stack.append(now)
            expressionArr = stack 

        answer = max(answer, abs(max(expressionArr)))
                         
        return
            
            
    for op in ["+","-","*"]:
        if op not in opRanks:
            opRanks.append(op)
            dfs(opRanks,expression)
            opRanks.remove(op)

