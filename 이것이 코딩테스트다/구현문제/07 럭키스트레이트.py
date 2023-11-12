s = input()
l = len(s)//2

sum1, sum2 = 0, 0
for i in range(l):
    sum1 += int(s[i])
    sum2 += int(s[i+l])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
