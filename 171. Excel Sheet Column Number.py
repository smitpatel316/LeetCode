class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s.upper()
        letter_to_pos = {
            k: v for (v, k) in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1)
        }

        col = 0
        for c in s:
            col = 26 * col + letter_to_pos[c]
        return col
