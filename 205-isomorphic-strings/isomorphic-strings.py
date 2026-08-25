class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        j = 0
        table = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in table:
                if table[s[i]]!=t[j]:
                    return False
            elif t[j] in table.values():
                return False
            else:
                table[s[i]]=t[j]
            j+=1
        return True
