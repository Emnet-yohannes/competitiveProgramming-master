class Solution:
    ctr = 0;
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort();
        print(nums)
        notFixed = True
        while notFixed:
            counter = 0
            for i in range(1,len(nums)-1):
                if(nums[i]!=nums[i+1]):
                    if((nums[i+1]+nums[i-1])/2==nums[i]):
                        nums[i],nums[i+1]=nums[i+1],nums[i]
                        counter +=1
                else:
                    if((nums[i+1]+nums[i-1])/2==nums[i]):
                        nums[i],nums[i-1]=nums[i-1],nums[i]
                        counter +=1
            if(counter == 0):
                notFixed =False
            else:
                notFixed = True
        return nums
