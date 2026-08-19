class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        j =0
        answer = float('inf')
        for i in range(len(nums)):
            sum+=nums[i]

            while sum>=target:
                if i-j+1<answer:
                    answer = i-j+1
                sum-=nums[j]
                j+=1
        if answer == float('inf'):
            return 0

        return answer       
                



