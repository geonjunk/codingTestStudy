import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

stack = deque()
for i in range(n):
    commands =  sys.stdin.readline().split()
    if commands[0]=="push":
        stack.appendleft(commands[1])
    elif commands[0]=="pop":
        if stack:
            print(stack.popleft())
        else:
            print("-1")
    
    elif commands[0]=="size":
        print(len(stack))
    elif commands[0]=="top":
        if stack:
            print(stack[0])
        else:
            print("-1")
    elif commands[0] == "empty":
        if stack:
            print("0")
        else:
            print("1")