
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r = n - 1
        dp = deque()
        op = 0
        res = 0

        for l in range(n - 1, -1, -1):
            nsize = 1

            while dp and nums[l] >= dp[-1][0]:
                height, size = dp.pop()
                op += (nums[l] - height) * size
                nsize += size

            dp.append([nums[l], nsize])

            while op > k:
                op -= dp[0][0] - nums[r]
                dp[0][1] -= 1

                if dp[0][1] == 0:
                    dp.popleft()

                r -= 1

            res += r - l + 1

        return res
