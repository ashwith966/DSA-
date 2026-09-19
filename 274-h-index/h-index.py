class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n-i<=v:
                return n-i
        return 0