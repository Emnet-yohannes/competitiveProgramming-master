class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        emptyArray =[0]*9
        print(emptyArray)
        for i in range(len(nums)):
            emptyArray[nums[i]]+=1
        sum = 0
        for j in range(len(emptyArray)):
            sum+=emptyArray[j]
            emptyArray[j]=sum
        newList = [0]*len(nums)
        for k in range(len(nums)):
            newList[emptyArray[nums[k]]-1]=nums[k]
            emptyArray[nums[k]]-=1
        nums.clear()
        nums.extend(newList)
        
        