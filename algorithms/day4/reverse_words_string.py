"""https://leetcode.com/problems/reverse-words-in-a-string-iii/"""


class Solution:
    def reverseWords(self, s):
        return ' '.join([w[::-1] for w in s.split()])


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    sol = Solution()
    print(sol.reverseWords(s))

