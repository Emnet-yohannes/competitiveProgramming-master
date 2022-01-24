def gradingStudents(grades):
    # Write your code here
    newGrade = []
    for x in range(0,len(grades)):
        if(grades[x]<38):
            newGrade.append(grades[x])
        else:
            if((grades[x]-grades[x]+(5-grades[x]%5))<3):
                newValue = grades[x]+(5-grades[x]%5)
                newGrade.append(newValue)
            else:
                newGrade.append(grades[x])
                
    #print(newGrade)
    return newGrade
#gradingStudents([68,87,45,34])