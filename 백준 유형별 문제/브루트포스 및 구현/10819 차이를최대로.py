n = int(input())
numbers = list(map(int,input().split()));
visited = [False]*(n)
answer = 0

def dfs(arr):
    global answer
    if len(arr) == n:
        result = 0
        for i in range(n-1):
            result+=abs(arr[i]-arr[i+1])
        answer = max(result,answer)
        return
    
    for i in range(n):
        if not visited[i]:
            arr.append(numbers[i])
            visited[i]=True
            dfs(arr)
            arr.pop()
            visited[i]=False

dfs([])
print(answer)
