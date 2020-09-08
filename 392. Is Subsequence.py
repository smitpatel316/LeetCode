class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        if s and not t:
            return False

        if not s:
            return True

        if len(s) == 1:
            return s in t

        if s[0] not in t:
            return False
        _index = t.index(s[0])

        return self.isSubsequence(s[1:], t[_index + 1 :])
