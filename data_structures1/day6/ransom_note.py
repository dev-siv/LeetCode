from collections import Counter


def canConstruct(ransomeNote, magazine):
    rn = Counter(ransomeNote)
    mg = Counter(magazine)
    for k, v in rn.items():
        val = mg.get(k, None)
        if val is None:
            return False
        elif val < v:
            return False
    return True


if __name__ == "__main__":
    rn = "aa"
    mg = "ab"
    print(canConstruct(rn, mg))
