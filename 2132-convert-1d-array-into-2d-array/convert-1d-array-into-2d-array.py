class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original)!=m*n:
            return []
        
        index=0
        a=[[0]*n for i in range (m)]
        for i in range (m):
            for j in range (n):
                a[i][j]=original[index]
                index+=1
        return a