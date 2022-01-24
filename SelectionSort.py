
class Solution: 
    def select(self, arr, i):
        # code here 
        min = arr[i]
        minIndex = i
        for k in range(i+1,len(arr)):
            if(arr[k]<min):
                min=arr[k]
                minIndex=k
        # print("my min {}" .format(min))
        # value = min(arr)
        return minIndex
    
    def selectionSort(self, arr,n):
        #code here
        for j in range(0,n-1):
            theMin = self.select(arr,j)
            temp = arr[j]
            arr[j]=arr[theMin]
            arr[theMin]=temp
            # print("haha {}" .format(arr))
        return arr
            
            