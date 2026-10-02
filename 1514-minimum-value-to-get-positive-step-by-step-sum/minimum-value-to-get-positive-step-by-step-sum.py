class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        Sum, ans = 0, 0
        for i in nums:
            Sum = Sum + i
            ans = min(ans, Sum)
        return -ans + 1
            
        
        

