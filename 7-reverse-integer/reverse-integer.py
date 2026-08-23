# class Solution:
#     def reverse(self, x: int) -> int:
#         if x>100000000:
#             return 0
#         count =0
#         if x<0:
#             x*=-1
#             count+=1
#         text = str(x)
#         output = []
#         for i in range(len(text)-1,-1,-1):
#             if text[i]==0:
#                 continue
#             else:
#                 output.append(text[i])
#         result = int("".join(output))
#         if count>0:
#             result*=-1  
#         return result  
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        res = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if (res > (2 ** 31 - 1) // 10) or (res == (2 ** 31 - 1) // 10 and digit > 7):
                return 0
            res = (res * 10) + digit

        return -res if is_negative else res
            

