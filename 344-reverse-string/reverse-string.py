class Solution:
    def reverseString(self, s: list[str]) -> None:
        j = len(s)-1
        for i in range (len(s)-1):
            if i<j:
                s[i],s[j]=s[j],s[i]
                j-=1

            


        