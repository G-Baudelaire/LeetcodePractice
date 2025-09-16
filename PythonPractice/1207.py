from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = defaultdict(lambda: 0)

        for i in arr:
            dictionary[i] += 1

        return len(set(dictionary.items())) == len(set(dictionary.values()))
