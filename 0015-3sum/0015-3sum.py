
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        l = []
        nums.sort()

        for k in range(len(nums) - 2):

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i, j = k + 1, len(nums) - 1

            while i < j:

                total = nums[k] + nums[i] + nums[j]

                if total < 0:
                    i += 1

                elif total > 0:
                    j -= 1

                else:
                    l.append([nums[k], nums[i], nums[j]])

                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

        return l
