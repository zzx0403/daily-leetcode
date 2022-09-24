class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {n[0]:m for m,n in enumerate(pieces)}
        idx = 0
        while idx < len(arr):
            if arr[idx] not in mp: #查找arr的第idx个值是否mp的key里面
                return False
            for j in pieces[mp[arr[idx]]]:  #遍历pieces中arr[idx]在mp中表示的索引对应的value
                if j != arr[idx]: #不相同则返回False
                    return False
                idx +=1     #相同则比较pieces中切片出来的下一个值    
        return True