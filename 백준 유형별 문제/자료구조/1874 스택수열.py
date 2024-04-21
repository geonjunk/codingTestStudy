from collections import deque
n=int(input())

stack =deque()
answer =[]
now = 1
answerFlag = True
numbers =[]
for i in range(n):
    numbers.append(int(input()))

for i in range(n):
    num = numbers[i]
    while now<=num:
        stack.appendleft(now)
        answer.append("+")
        now+=1
    if stack[0]==num:
        answer.append("-")
        stack.popleft()
    else:
        answerFlag=False
        break

if answerFlag:
    for a in answer:
        print(a) 
else:
    print("NO")
  
