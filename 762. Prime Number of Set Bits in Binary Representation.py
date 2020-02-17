class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        counter = 0
        for i in range(L, R + 1):
            binary = str(bin(i)[2:])
            if binary.count("1") in primes:
                counter += 1
        return counter
