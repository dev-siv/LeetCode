"""https://leetcode.com/problems/reverse-string/"""

class Solution:
    def reverseString(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        print(s)


if __name__ == "__main__":
    s = Solution()
    s.reverseString(["h", "e", "l", "l"])
