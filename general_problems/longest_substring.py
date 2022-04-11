def lengthOfLongestSubstring(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == len(set(s)):
        return len(s)


if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))
