class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if  len(nums) == 1:
            return nums[0]

        p_minus_2, p_minus_1 = nums[0], max(nums[0], nums[1])
        maximum = p_minus_1
        for i in range(2, len(nums)):
            maximum = max(p_minus_2 + nums[i], p_minus_1)
            p_minus_2, p_minus_1 = p_minus_1, maximum
        return maximum