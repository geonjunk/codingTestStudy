str = input()
ans = 0

numbers = [0]*10

for s in str:
    idx = int(s)
    if numbers[idx]==0:
        if idx==6 and numbers[9]>0:
            idx = 9
        elif idx==9 and numbers[6]>0:
            idx = 6
        else:
            ans+=1
            for i in range(10):
                numbers[i]+=1
    
    numbers[idx]-=1

print(ans)
