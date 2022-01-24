class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        myArray = []
        nums.sort()
        # print(nums)
        for i in range(len(nums)):
            if(target == nums[i]):
                myArray.append(i)
        # print(myArray)
        return myArray