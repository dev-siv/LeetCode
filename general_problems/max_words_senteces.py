"""https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/"""


def mostWordsFound(sentences):
    return max([len(word.split()) for word in sentences])