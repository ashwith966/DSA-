class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if i == len(nums)-1:
                    return max(count,max_num)
            if nums[i]!=1:
                max_num=max(count,max_num)
                count = 0   
        return max_num