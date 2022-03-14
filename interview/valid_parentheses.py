def isValid(s):
    valid = ["()", "{}", "[]"]
    if len(s) % 2 != 0:
        return False
    while len(s) != 0:
        n = len(s)
        s = s.replace(valid[0], "").replace(valid[1], "").replace(valid[2], "")
        if n == len(s):
            return False

    return not s


def isValid2(s):
    valid = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    if len(s) % 2 != 0:
        return False
    n = len(s)
    first_half = s[0:n//2]
    second_half = s[n//2:]
    result = ""
    for letter in first_half:
        result = valid[letter] + result
    print(result)


print(isValid("()"))
isValid2("{}[]")
