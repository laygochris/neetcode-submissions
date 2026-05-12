class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n < 0:
                return 0
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = solve(n-2) + solve(n-1)
            return memo[n]
        return(solve(n))