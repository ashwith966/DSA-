class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k ==1:
            return 0
        
        diff = float('inf')

        nums.sort()

        for i in range(len(nums)-k+1):
            curr_diff = nums[i+k-1]-nums[i]
            diff = min(diff,curr_diff)

        return diff
                 
                