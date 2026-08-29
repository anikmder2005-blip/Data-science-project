from typing import List
from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)

        curr_group = 0
        num_to_group = {}
        group_to_list = {}

        num_to_group[nums_sorted[0]] = curr_group
        group_to_list[curr_group] = deque([nums_sorted[0]])

        for i in range(1, len(nums_sorted)):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                curr_group += 1
                group_to_list[curr_group] = deque()

            num_to_group[nums_sorted[i]] = curr_group
            group_to_list[curr_group].append(nums_sorted[i])

        for i in range(len(nums)):
            num = nums[i]                  # FIX
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums