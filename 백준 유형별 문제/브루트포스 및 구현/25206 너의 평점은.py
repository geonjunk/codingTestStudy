totPoints = 0
totGrades = 0
for _ in range(20):
    subject,point,grade = input().split()

    if grade!="P":
        nowPoint = float(point)
        totPoints+=nowPoint
        if grade =="A+":
            nowGrade = 4.5
        elif grade =="A0":
            nowGrade = 4
        elif grade =="B+":
            nowGrade = 3.5
        elif grade =="B0":
            nowGrade = 3
        elif grade =="C+":
            nowGrade = 2.5
        elif grade =="C0":
            nowGrade = 2
        elif grade =="D+":
            nowGrade = 1.5
        elif grade =="D0":
            nowGrade = 1
        elif grade=="F":
            nowGrade = 0
        
        totGrades+=(nowPoint*nowGrade)

print(totGrades/totPoints)
