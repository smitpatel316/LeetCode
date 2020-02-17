class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        counter = len(x) - 1
        for i in range(int(len(x)/2)):
            if x[i] != x[counter]:
                return False
            counter -= 1
        return True