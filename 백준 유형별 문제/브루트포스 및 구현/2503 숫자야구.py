n = int(input())

arr = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i!=j and i!=k and j!=k:
                arr.append(str(i)+str(j)+str(k))

for i in range(n):
    num,s,b = input().split() 
    ansArr=[]
    for a in arr:
        sCnt,bCnt = 0,0
        for j in range(len(num)):
            if num[j] in a:
                if num[j]==a[j]:
                    sCnt+=1
                else:
                    bCnt+=1
        if sCnt==int(s) and bCnt==int(b):
            ansArr.append(a)
    arr = ansArr

print(len(arr))
