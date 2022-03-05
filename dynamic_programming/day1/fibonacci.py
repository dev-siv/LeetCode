class Solution:
    def fib(self, n, memo={}):
        # establish base case
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = self.fib(n - 2) + self.fib(n - 1)
        return memo[n]


s = Solution()
print(s.fib(8))
