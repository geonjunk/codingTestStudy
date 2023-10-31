n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()


def calArr(h):
    result = 0
    for i in arr:
        if i > h:
            result += (i-h)
    return result


def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start+end)//2
        now = calArr(mid)
        if now >= m:
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


print(binary_search(arr[0], arr[n-1]))
