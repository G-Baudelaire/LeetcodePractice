# Container With Most Water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        distance = right_pointer

        while distance > 0:
            new_area = distance * min(height[left_pointer], height[right_pointer])
            if new_area > max_area:
                max_area = new_area

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

            distance -= 1
        return max_area


if __name__ == '__main__':
    height = [1, 2, 4, 3]
    print(Solution().maxArea(height))
