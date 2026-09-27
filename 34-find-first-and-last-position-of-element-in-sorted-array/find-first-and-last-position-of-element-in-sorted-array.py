class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    def binSearch(self, nums, target, leftbias):
        l = 0
        r = len(nums) - 1
        i = -1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m

                if leftbias:
                    r = m - 1
                else:
                    l = m + 1

        return i