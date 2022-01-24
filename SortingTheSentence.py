class Solution:
    def sortSentence(self, s: str) -> str:
        myArray = s.split(" ")
        sortedArray = ["a"]*len(myArray)
        for x in myArray:
            print(x[-1])
            sortedArray[int(x[-1])-1]=x[:-1]
        print(sortedArray)
        myString =""
        for j in range(len(sortedArray)):
            if(j==len(sortedArray)-1):
                myString+=sortedArray[j]
            else:
                myString+=sortedArray[j]+" "
            
        print(myString)
        return myString