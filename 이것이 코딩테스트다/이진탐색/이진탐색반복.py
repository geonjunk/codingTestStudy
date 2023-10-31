N, M = map(int, input().split())
arr = list(map(int, input().split()))


start = 0
end = N-1


def binary_search(start, end):
    result = -1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > M:
            end = mid-1
        elif arr[mid] == M:
            result = mid
            break
        else:
            start = mid+1

    return result


print(binary_search(start, end)+1)
