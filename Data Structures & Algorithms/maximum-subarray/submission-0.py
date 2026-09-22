class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]

        for i in range(len(nums)):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                res = max(curr, res)
        
        return res