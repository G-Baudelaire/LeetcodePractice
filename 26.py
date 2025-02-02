class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer1 = 0
        current_val = None
        for pointer2 in range(len(nums)):
            if nums[pointer2] == current_val:
                continue

            nums[pointer1] = nums[pointer2]
            current_val = nums[pointer2]
            pointer1 += 1

        return pointer1


nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))
print(nums)
