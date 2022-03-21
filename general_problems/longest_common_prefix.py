def longestCommonPrefix(strs):
    if not strs:
        return ""
    min_str, max_str = min(strs), max(strs)
    for index, char in enumerate(min_str):
        if char != max_str[index]:
            return min_str[:index]
    return min_str


if __name__ == "__main__":
    s = ["acb", "a", "bccasa"]
    print(longestCommonPrefix(s))
