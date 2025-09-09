class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = "AEIOUaeiou"
        output = ""

        for character in s:
            if character in vowels:
                stack.append(character)

        for index in range(len(s)):
            output += stack.pop() if s[index] in vowels else s[index]

        return output
