from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        output = []
        for i in range(len(nums)):
            endings = self.permute(nums[:i] + nums[i + 1:])
            output.extend([nums[i]] + end for end in endings)
        return output


nums = [1, 2, 3]
print(Solution().permute(nums))
