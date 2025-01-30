from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionary = defaultdict(lambda: 0)
        for i in range(len(s)):
            dictionary[s[i]] -= 1
            dictionary[t[i]] += 1
        return not any(dictionary.values())
