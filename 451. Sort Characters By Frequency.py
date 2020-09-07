from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        most_common = c.most_common()
        res = ""

        for (c, count) in most_common:
            res += c * count

        return res


if __name__ == "__main__":
    print(Solution().frequencySort("Aabb"))
