class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean String of non-alphanumeric characters
        s = [char for char in s.lower() if char.isalnum()]
        return all(s[i] == s[-(i + 1)] for i in range(len(s) // 2))


if __name__ == '__main__':
    test = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(test))
