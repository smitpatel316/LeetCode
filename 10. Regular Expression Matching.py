import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.match(p, s):
            return re.match(p, s).group() == s
        else:
            return False
