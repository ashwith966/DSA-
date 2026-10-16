# class Solution:
#     def concatWithReverse(self, nums: list[int]) -> list[int]:
#         r = []
#         i  = 0
#         j = len(nums)-1
#         r.extend(nums)
#         while i<j:
#             nums[i],nums[j]=nums[j],nums[i]
#             i+=1
#             j-=1
#         r.extend(nums)
#         return r

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1, -1, -1):
            nums.append(nums[i])
        return nums