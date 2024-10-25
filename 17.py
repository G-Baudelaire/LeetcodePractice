import itertools


class Solution(object):
    character_dictionary = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6   ": "mno", "7": "pqrs",
                            "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        product_input = list(Solution.character_dictionary[i] for i in digits)
        join = lambda x: "".join(x)
        products = itertools.product(*product_input)
        return list(map(join, products))


print(Solution().letterCombinations("23"))
