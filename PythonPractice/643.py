from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        max_total = total

        for old, new in zip(range(len(nums) - k), range(k, len(nums))):
            total = total + nums[new] - nums[old]
            max_total = max(max_total, total)
        return max_total / k
