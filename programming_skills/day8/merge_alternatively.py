def mergeAlternately(word1, word2):
    i, j, m, n = 0, 0, len(word1), len(word2)
    result = ""
    while i < m or j < n:
        if i < m:
            result += word1[i]
            i += 1
        if j < n:
            result += word2[j]
            j += 1
    return result


if __name__ == "__main__":
    s1 = "Sivsai"
    s2 = "Gava"
    print(mergeAlternately(s1, s2))