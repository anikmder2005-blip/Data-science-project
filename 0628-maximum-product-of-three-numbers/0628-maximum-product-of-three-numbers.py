class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        # Sort the array in ascending order
        nums.sort()
        
        # Scenario 1: Product of the three largest numbers
        p1 = nums[-1] * nums[-2] * nums[-3]
        
        # Scenario 2: Product of the two smallest (negative) numbers and the largest number
        p2 = nums[0] * nums[1] * nums[-1]
        
        # Return the maximum of both possibilities
        return max(p1, p2)