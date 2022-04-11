def strStr(haystack, needle):
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1
    for index in range(len(haystack)):
        if needle == haystack[index:index+len(needle)]:
            return index
    return -1

if __name__ == "__main__":
    print(strStr("hello", "ll"))
