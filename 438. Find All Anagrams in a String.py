from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexes = []
        p_counter = Counter(p)
        s_counter = Counter()
        for (i, c) in enumerate(s):
            s_counter[c] += 1
            if i >= len(p):
                s_counter[s[i - len(p)]] -= 1
                if s_counter[s[i - len(p)]] == 0:
                    del s_counter[s[i - len(p)]]
            if s_counter == p_counter:
                indexes.append(i - len(p) + 1)
        return indexes
