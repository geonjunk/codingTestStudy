n = int(input())
arr = list(map(int, input().split()))
m = int(input())
parts = list(map(int, input().split()))
answer = []


def binary_search(start, end, now):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == now:
            return "yes"
        elif arr[mid] > now:
            end = mid-1
        else:
            start = mid+1
    return "no"


for p in parts:
    answer.append(binary_search(0, n-1, p))
for a in answer:
    print(a, end=" ")
