class Solution:
    def __init__(self):
        self.seen = {}

    def longestSubstring(self, s, k):
        if (s, k) in self.seen:
            return self.seen[(s, k)]
        for c in set(s):
            if s.count(c) < k:
                self.seen[(s, k)] = max(self.longestSubstring(t, k) for t in s.split(c))
                return self.seen[(s, k)]
        self.seen[(s, k)] = len(s)
        return self.seen[(s, k)]
