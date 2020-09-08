from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        occur = dict(Counter(s))
        for c in t:
            if c not in occur or occur[c] == 0:
                return False
            else:
                occur[c] -= 1

        for char in occur:
            if occur[char] != 0:
                return False

        return True
