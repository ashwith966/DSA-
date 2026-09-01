class Solution:
    def rotate(self, num: list[int], k: int) -> None:
        def fun(l,r):
            while l<r:
                num[l],num[r]=num[r],num[l]
                l+=1
                r-=1
        k = k%len(num)
        fun(0,len(num)-1)
        fun(0,k-1)
        fun(k,len(num)-1)
        
        