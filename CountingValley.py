def countingValleys(steps, path):
    # Write your code here
    counter = 0
    seaLevel = 0
    for i in range(steps):
        if(seaLevel == 0):
            if(path[i]=="D"):
                counter +=1
                seaLevel -=1
            elif(path[i]=="U"):
                seaLevel+=1
        else:
            if(path[i]=="U"):
                seaLevel+=1
            else:
                seaLevel-=1
    
    print(counter)
countingValleys(8,["D","D","U","U","U","U","D","D"])