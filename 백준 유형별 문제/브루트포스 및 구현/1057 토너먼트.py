n,x1,x2 = map(int,input().split())

r = 1
while x1%2+x1//2 != x2%2+x2//2:
    x1 = x1%2+x1//2 
    x2 = x2%2+x2//2
    r+=1

print(r)


n,x1,x2 = map(int,input().split())

r = 0
while x1 != x2:
    x1 -= x1//2
    x2 -= x2//2
    r+=1

print(r)