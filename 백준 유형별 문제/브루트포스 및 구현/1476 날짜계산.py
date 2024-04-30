e,s,m = map(int,input().split())

nowE,nowS,nowM = 0,0,0
cnt = 0
while True:
    cnt +=1
    nowE = nowE%15+1
    nowS = nowS%28+1
    nowM = nowM%19+1

    if e==nowE and s ==nowS and m == nowM:
        print(cnt)
        break
