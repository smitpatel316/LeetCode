class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for j in J:
            total += S.count(j)
        return total
