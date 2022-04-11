def lengthOfLongestSubstring(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == len(set(s)):
        return len(s)
    max_length = 0
    for i in range(len(s)):
        longest = s[i]
        # if max_length > len(s)-i:
        for j in range(i+1, len(s)):
            if s[j] in longest:
                break
            else:
                longest += s[j]
            if len(longest) > max_length:
                max_length = len(longest)
    return max_length


if __name__ == "__main__":
    print(lengthOfLongestSubstring("bbbb"))
