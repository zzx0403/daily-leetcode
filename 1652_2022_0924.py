class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k==0:
            return [0]*n
        ans = []
        code_new = code*2  #数组比较短，直接接一个
        for i in range(n):
            if k>0:
                ans.append(sum(code_new[i+1:i+k+1])) 
            else:
                ans.append(sum(code_new[i+n+k:n+i]))
        return ans