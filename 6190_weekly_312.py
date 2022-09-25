class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        dec = [1] * n  #递增
        for i in range(n - 2, k, -1): #从后往前遍历，当前位置向后有几个数非递减
            if nums[i] <= nums[i + 1]:
                dec[i] = dec[i + 1] + 1  # 递推
        inc = 1 #递减
        for i in range(1, n - k):
            if inc >= k and dec[i + 1] >= k: #当往前非递增的个数和往后非递减的个数，都大于K
                ans.append(i)
            if nums[i - 1] >= nums[i]:   #从前往后遍历，当前位置向前有几个数非递增
                inc += 1  # 递推
            else:  #假如不是非递增，初始化
                inc = 1
        return ans