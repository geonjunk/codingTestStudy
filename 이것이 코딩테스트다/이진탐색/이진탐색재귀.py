N, M = map(int, input().split())
arr = list(map(int, input().split()))


start = 0
end = N-1


def binary_search(start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] > M:
        return binary_search(start, mid-1)
    elif arr[mid] == M:
        return mid
    else:
        return binary_search(mid+1, end)


print(binary_search(start, end)+1)
