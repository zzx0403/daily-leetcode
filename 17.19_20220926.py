class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.append(-1)
        nums.append(-1)
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                nums.insert(i,i+1)
                ans.append(i+1)
        return ans