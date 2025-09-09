from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        product = 1
        for index in range(len(nums)):
            output[index] = product
            product *= nums[index]

        product = 1
        for index in reversed(range(len(nums))):
            output[index] *= product
            product *= nums[index]

        return output
