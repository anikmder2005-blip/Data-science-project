class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [-1] * n  # Initialize result array with -1
        stack = []  # Stack to store indices
        
        # Traverse the array twice to handle circular nature
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        
        return result