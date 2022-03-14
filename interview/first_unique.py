from collections import OrderedDict, Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Explaination: Ordered Dict will save the characters it encounters in
        # same sequence as the original string. Hence it becomes easy to catch hold of the first
        # unique character. Then according to the counter variable, whenever the first 1 is encountered
        # the corresponding dict.key's index is returned from the original String.
        for i, j in OrderedDict(Counter(s)).items():
            if j == 1:
                return s.index(i)
        return -1
