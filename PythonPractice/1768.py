class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        for character1, character2 in zip(word1, word2):
            output += character1
            output += character2

        output += word2[len(word1):] if len(word1) < len(word2) else word1[len(word2):]
        return output

    def mergeAlternately(self, word1: str, word2: str) -> str:
        from itertools import zip_longest
        output = ""
        for character1, character2 in zip_longest(word1, word2, fillvalue=""):
            output += character1 + character2
        return output
