from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replace_pointer = 0

        for index in range(len(nums)):
            while (replace_pointer < index and nums[replace_pointer] != 0):
                replace_pointer += 1

            nums[replace_pointer], nums[index] = nums[index], nums[replace_pointer]
