class Solution:
    def rotatedDigits(self, n: int) -> int:
        def check(num):
            change = False
            rem = 0 #取余
            mod = num #取模
            while mod>0:
                rem = mod%10
                mod = mod//10
                if rem in [3,4,7]:
                    return False
                if rem in [2,5,6,9]:
                    change  = True
            if change:
                return True
            else:
                return False
        ans = 0
        for i in range(1,n+1):
            if check(i):
                ans+=1
        return ans