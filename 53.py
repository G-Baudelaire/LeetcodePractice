from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float('-inf')
        current_sum = 0

        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
