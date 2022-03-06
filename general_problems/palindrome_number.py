"""
https://leetcode.com/problems/palindrome-number/
"""
import time


class Solution:
    def isPalindrome(self, x):
        reverse = 0
        while x != 0:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x //= 10

        return reverse == x

    def palindrome(self, x):
        if x < 0:
            return False

        return int(str(x)[::-1]) == x


s = Solution()
start = time.time()
print(s.isPalindrome(111111111111111111111111111111111111111111111111111111111111111111))
val1 = time.time() - start
print(f"1st: {time.time() - start}")
start = time.time()
print(s.palind(111111111111111111111111111111111111111111111111111111111111111111))
val2 = time.time() - start
print(f"2st: {time.time() - start}")
print(val2 < val1)
