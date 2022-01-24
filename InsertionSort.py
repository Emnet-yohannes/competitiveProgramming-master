def checker():
    array = [6,3,2,5,4,1]
    #[3,5,2,4]
    for i in range(1,len(array)):
        value =  array[i]
        j=i
        while j >= 1:
            if value<array[j-1]:
                array[j]=array[j-1]
                array[j-1]=value
                j-=1
            else:
                j-=1
    print(array)
checker()
