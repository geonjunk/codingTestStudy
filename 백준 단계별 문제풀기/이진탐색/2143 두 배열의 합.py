T = int(input())

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

aSum, bSum = [], []
ans = 0
dictA = dict()
for i in range(n):
    now = arr1[i]
    aSum.append(arr1[i])
    for j in range(i+1, n):
        now += arr1[j]
        aSum.append(now)
for i in range(m):
    now = arr2[i]
    bSum.append(arr2[i])
    for j in range(i+1, m):
        now += arr2[j]
        bSum.append(now)

for i in range(len(aSum)):
    if aSum[i] in dictA.keys():
        dictA[aSum[i]] += 1
    else:
        dictA[aSum[i]] = 1

for i in range(len(bSum)):
    now = T-bSum[i]
    if now in dictA.keys():
        ans += dictA[now]

print(ans)