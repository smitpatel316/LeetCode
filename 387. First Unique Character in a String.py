from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for (index, c) in enumerate(s):
            if counter[c] == 1:
                return index
        return -1
