def findTheDifference(s, t):
    for l in t:
        if s.count(l) != t.count(l):
            return l



if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(findTheDifference(s, t))
