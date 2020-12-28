from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not k:
            return []

        freq = [None] * len(words)
        counter = Counter(words)

        for word in counter:
            if freq[counter[word]] is None:
                freq[counter[word]] = []
            freq[counter[word]].append(word)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            if not k:
                break
            if freq[i] is not None:
                if len(freq[i]) > 1:
                    freq[i].sort()
                for w in freq[i]:
                    if not k:
                        break
                    res.append(w)
                    k -= 1
        return res


if __name__ == "__main__":
    print(
        Solution().topKFrequent(
            [
                "glarko",
                "zlfiwwb",
                "nsfspyox",
                "pwqvwmlgri",
                "qggx",
                "qrkgmliewc",
                "zskaqzwo",
                "zskaqzwo",
                "ijy",
                "htpvnmozay",
                "jqrlad",
                "ccjel",
                "qrkgmliewc",
                "qkjzgws",
                "fqizrrnmif",
                "jqrlad",
                "nbuorw",
                "qrkgmliewc",
                "htpvnmozay",
                "nftk",
                "glarko",
                "hdemkfr",
                "axyak",
                "hdemkfr",
                "nsfspyox",
                "nsfspyox",
                "qrkgmliewc",
                "nftk",
                "nftk",
                "ccjel",
                "qrkgmliewc",
                "ocgjsu",
                "ijy",
                "glarko",
                "nbuorw",
                "nsfspyox",
                "qkjzgws",
                "qkjzgws",
                "fqizrrnmif",
                "pwqvwmlgri",
                "nftk",
                "qrkgmliewc",
                "jqrlad",
                "nftk",
                "zskaqzwo",
                "glarko",
                "nsfspyox",
                "zlfiwwb",
                "hwlvqgkdbo",
                "htpvnmozay",
                "nsfspyox",
                "zskaqzwo",
                "htpvnmozay",
                "zskaqzwo",
                "nbuorw",
                "qkjzgws",
                "zlfiwwb",
                "pwqvwmlgri",
                "zskaqzwo",
                "qengse",
                "glarko",
                "qkjzgws",
                "pwqvwmlgri",
                "fqizrrnmif",
                "nbuorw",
                "nftk",
                "ijy",
                "hdemkfr",
                "nftk",
                "qkjzgws",
                "jqrlad",
                "nftk",
                "ccjel",
                "qggx",
                "ijy",
                "qengse",
                "nftk",
                "htpvnmozay",
                "qengse",
                "eonrg",
                "qengse",
                "fqizrrnmif",
                "hwlvqgkdbo",
                "qengse",
                "qengse",
                "qggx",
                "qkjzgws",
                "qggx",
                "pwqvwmlgri",
                "htpvnmozay",
                "qrkgmliewc",
                "qengse",
                "fqizrrnmif",
                "qkjzgws",
                "qengse",
                "nftk",
                "htpvnmozay",
                "qggx",
                "zlfiwwb",
                "bwp",
                "ocgjsu",
                "qrkgmliewc",
                "ccjel",
                "hdemkfr",
                "nsfspyox",
                "hdemkfr",
                "qggx",
                "zlfiwwb",
                "nsfspyox",
                "ijy",
                "qkjzgws",
                "fqizrrnmif",
                "qkjzgws",
                "qrkgmliewc",
                "glarko",
                "hdemkfr",
                "pwqvwmlgri",
            ],
            14,
        )
    )
