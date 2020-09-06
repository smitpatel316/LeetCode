class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0
        while n != 0:
            hamming_weight += 1
            n &= n - 1
        return hamming_weight


if __name__ == "__main__":
    print(Solution().hammingWeight(0o0000000000000000000000000001011))
