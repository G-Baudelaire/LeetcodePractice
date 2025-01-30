from collections import defaultdict
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = defaultdict(lambda: 0)
        for i in nums:
            if dictionary[i] == 0:
                dictionary[i] += 1
            else:
                return True
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()

        for number in nums:
            if number in unique_nums:
                return True
            unique_nums.add(number)
        return False