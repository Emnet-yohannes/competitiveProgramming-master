class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        newArray = []
        for i  in range(len(l)):
            newArray.append(self.checkArthimetic(nums[l[i]:r[i]+1]))
        # print(newArray)
        return newArray
        
        
        
    def checkArthimetic(self,arr:List[int]):
        arr.sort()
        print(arr)
        d = arr[1]-arr[0]
        print(d)
        for j in range(len(arr)-1):
            if(arr[j+1]-arr[j]!=d):
                return False
            
        return True