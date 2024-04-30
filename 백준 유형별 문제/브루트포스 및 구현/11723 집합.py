import sys
input = sys.stdin.readline
m = int(input())
s = set()
for i in range(m):
    c = list(input().split())

    if len(c)==1:
        if c[0]=='all':
            s.clear()
            for i in range(1,21):
                s.add(str(i))
        elif c[0]=='empty':
            s.clear()
    else:
        if c[0]=='add':
            s.add(c[1])
        elif c[0]=='remove' and c[1] in s:
            s.remove(c[1])
        elif c[0]=='check':
            if c[1] in s:
                print(1)
            else:
                print(0)
        elif c[0]=='toggle':
            if c[1] in s:
                s.remove(c[1])
            else:
                s.add(c[1])