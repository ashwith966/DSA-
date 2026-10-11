class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]<target:
        #             res+=1
        # return res

        res = 0
        nums.sort()
        r = len(nums)-1
        l = 0
        while(l!=r):
            if (nums[l]+nums[r]<target):
                res+=r-l
                l+=1
            else:
                r-=1
        return res