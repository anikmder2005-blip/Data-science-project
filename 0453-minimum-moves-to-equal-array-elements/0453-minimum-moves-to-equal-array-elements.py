class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        res = 0 

        for n in  nums:
            res += n - mn

        return res