class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        for word in reversed(words):
            if not word:
                return len(word)