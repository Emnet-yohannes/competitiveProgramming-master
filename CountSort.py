def checker():
    myArray =[1,4,1,2,7,5,2]
    emptyArray = [0,0,0,0,0,0,0,0,0,0]
    for j in range(0,len(myArray)):
        emptyArray[myArray[j]] +=1
    sum = 0;
    for i in range(0,len(emptyArray)):
        sum += emptyArray[i]
        emptyArray[i]=sum
    # print(emptyArray)
    # print(myArray)
    answer=[0,0,0,0,0,0,0]
    for k in range(0,len(myArray)):
        # answer.insert(emptyArray[myArray[k]],myArray[k])
        indexer = emptyArray[myArray[k]]-1
        answer[indexer]=myArray[k]
        emptyArray[myArray[k]]-=1
        # print(emptyArray)
    print(f'answer{answer}')
        
checker()