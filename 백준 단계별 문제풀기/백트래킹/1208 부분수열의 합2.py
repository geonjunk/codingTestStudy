n, s = map(int, input().split())
arr = list(map(int, input().split()))

leftSumArr = []
rightSumArr = []


def calLeftSum(count, now):
    if count == n//2:
        leftSumArr.append(now)
        return

    calLeftSum(count+1, now+arr[count])
    calLeftSum(count+1, now)


def calRightSum(count, now):
    if count == n:
        rightSumArr.append(now)
        return

    calRightSum(count+1, now+arr[count])
    calRightSum(count+1, now)


calLeftSum(0, 0)
calRightSum(n//2, 0)
leftSumArr.sort()
rightSumArr.sort()

ans = 0


def binary_search_left(sumArr, num):
    left = 0
    right = len(sumArr)-1

    while left <= right:
        mid = (left+right)//2
        if sumArr[mid] >= num:
            right = mid-1
        else:
            left = mid+1

    return left


def binary_search_right(sumArr, num):
    left = 0
    right = len(sumArr)-1

    while left <= right:
        mid = (left+right)//2
        if sumArr[mid] <= num:
            left = mid+1
        else:
            right = mid-1

    return left


for i in range(len(leftSumArr)):
    now = s-leftSumArr[i]
    ans += (binary_search_right(rightSumArr, now) -
            binary_search_left(rightSumArr, now))

if s == 0:
    print(ans - 1)
else:
    print(ans)
# 반반 나눠서 sum을 구함
