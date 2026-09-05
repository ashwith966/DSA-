class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1 + nums2
        result.sort()
        j = len(result)
        if len(result)%2!=0:
            return result[j//2]
            
        else:
            k = result[(j//2)] + result[(j//2)-1]
            return float(k/2)
