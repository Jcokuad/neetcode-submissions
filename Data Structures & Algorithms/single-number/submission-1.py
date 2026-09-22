class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0 # store our xor results n ^ 0 = n
        for n in nums:
            res = n ^ res
        return res

