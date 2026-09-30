class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        new = [0]*(len(nums))
        sum = nums[0]
        new[0]=nums[0]
        for i in range(1,len(nums)):
            sum+=nums[i]
            new[i]=sum
        return new

            
