def longestPalindrome(s):
    palindromes = {}
    max_length = 0
    for index in range(len(s)+1):
        for j in range(index, len(s)+1):
            substring = s[index:j]
            if substring == substring[::-1]:
                palindromes[substring] = len(substring)
                if len(substring) > max_length:
                    max_length = len(substring)
    print(palindromes)
    return [k for k,v in palindromes.items() if v == max_length][0]


if __name__ == "__main__":
    inp = "abb"
    print(longestPalindrome(inp))


