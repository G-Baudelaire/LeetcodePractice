from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        right_total = sum(nums[1:])
        left_total = 0

        if right_total == left_total:
            return 0

        for index in range(1, len(nums)):
            right_total -= nums[index]
            left_total += nums[index - 1]
            if left_total == right_total:
                return index

        return -1
