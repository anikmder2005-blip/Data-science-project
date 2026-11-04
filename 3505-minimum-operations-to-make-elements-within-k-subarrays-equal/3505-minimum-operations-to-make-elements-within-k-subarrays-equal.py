from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        left, right = [], []
        delayed = defaultdict(int)

        left_size = right_size = 0
        sum_l = sum_r = 0

        ops = [0] * n

        def prune(h, sign):
            while h and delayed[sign * h[0]]:
                delayed[sign * h[0]] -= 1
                heappop(h)

        def balance():
            nonlocal left_size, right_size, sum_l, sum_r

            if left_size > right_size + 1:
                num = -heappop(left)

                heappush(right, num)
                sum_r += num
                sum_l -= num

                left_size -= 1
                right_size += 1

                prune(left, -1)

            elif left_size < right_size:
                num = heappop(right)

                heappush(left, -num)
                sum_l += num
                sum_r -= num

                left_size += 1
                right_size -= 1

                prune(right, 1)

        # Sliding window
        for i, value in enumerate(nums):

            if not left or value <= -left[0]:
                heappush(left, -value)
                sum_l += value
                left_size += 1
            else:
                heappush(right, value)
                sum_r += value
                right_size += 1

            # Remove element outside the window
            if i >= x:
                value_to_remove = nums[i - x]

                delayed[value_to_remove] += 1

                if value_to_remove <= -left[0]:
                    left_size -= 1
                    sum_l -= value_to_remove

                    if value_to_remove == -left[0]:
                        prune(left, -1)

                else:
                    right_size -= 1
                    sum_r -= value_to_remove

                    if right and value_to_remove == right[0]:
                        prune(right, 1)

            balance()

            # Calculate minimum operations for window
            if i >= x - 1:
                mid = -left[0]

                cost = (
                    mid * left_size - sum_l
                    + sum_r - mid * right_size
                )

                ops[i] = cost

        # Dynamic Programming
        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for j in range(1, k + 1):
            for i in range(j * x, n + 1):

                dp[i][j] = min(
                    dp[i - 1][j],
                    dp[i - x][j - 1] + ops[i - 1]
                )

        return dp[n][k]