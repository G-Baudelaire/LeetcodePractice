class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]

        if n in (0, 1, 2):
            return dp[n]

        term = 2
        while (n != term):
            dp = [dp[1], dp[2], sum(dp)]
            term += 1

        return dp[-1]
