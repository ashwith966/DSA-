class Solution:
    def checkDivisibility(self, n: int) -> bool:
        text = str(n)
        product = 1
        sum =0
        for i in range(len(text)):
                sum+=int(text[i])
                product*=int(text[i])
        if n%(product+sum)==0:
            return True
        else:
             return False



