from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not k:
            return []
        c = Counter(words)
        most_common = c.most_common()
        most_common.sort(key=lambda x: (x[1] * -1, x[0]))
        return [most_common[i][0] for i in range(k)]


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
