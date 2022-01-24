class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        initial = 0
        final = len(nums)-1
        maxi = 0
        while initial < len(nums)/2:
            if(nums[initial]+nums[final] > maxi):
                maxi = nums[initial]+nums[final]
                initial+=1
                final-=1
            else:
                initial+=1
                final-=1
        return maxi
            