x,y = map(int,input().split())
n = int(input())
pos = []
nowX,nowY = 0,0
for i in range(n+1):
    d,l = map(int,input().split()) 
    if d==1:
        nowPos = (l,0)
    elif d==2:
        nowPos = (l,y)
    elif d==3:
        nowPos = (0,l)
    else:
        nowPos = (x,l)
    if i<n:
        pos.append(nowPos)
    else:
        nowX,nowY = nowPos

ans = 0


for (px,py) in pos:
    if abs(nowX-px)==x:
        ans+= min(x+nowY+py,x+(y-nowY)+(y-py))
    elif abs(nowY-py)==y:
        ans+= min(y+nowX+px,y+(x-nowX)+(x-px))
    else:
        ans+= abs(nowX-px)+abs(nowY-py)    
print(ans)
