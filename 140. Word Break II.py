from typing import List


class Solution:
    def __init__(self):
        self.seen = dict()

    def wordBreak(self, s: str, wordDict):
        if not s:
            return []

        word_dict = set(wordDict)

        if s in word_dict:
            temp_dict = word_dict
            temp_dict.remove(s)
            return [s] + self.wordBreak(s, temp_dict)

        if s in self.seen:
            return self.seen[s]

        sentences = []
        for i in range(len(s)):
            _s = s[: i + 1]
            if _s in word_dict:
                for perm in self.wordBreak(s[i + 1 :], word_dict):
                    sentences.append(f"{_s} {perm}")

        self.seen[s] = sentences
        return sentences


if __name__ == "__main__":
    print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(
        Solution().wordBreak(
            "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
        )
    )
    print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak("aaaaaaa", ["aaaa", "aa", "a"]))
