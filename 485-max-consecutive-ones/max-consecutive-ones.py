class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        count = 0
        for num in nums:
            if num ==1:
                count+=1
                max_num=max(count,max_num)
            else:
                count =0 
        return max_num