"""
https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def intToRoman(self, num):
        romans = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        if num in romans:
            return romans[num]
        for letter in str(num)[::-1]:
            print(letter)


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(1994))
