# Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        state = nums[0]
        for num in nums[1:]:
            state = state ^ num
        return state
