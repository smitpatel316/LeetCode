class Solution:
    def __init__(self):
        self.dp = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, set(wordDict))

    def dfs(self, word, word_dict):
        if not word:
            return True
        if not word_dict and word:
            return False
        if word in self.dp:
            return self.dp[word]
        for i in range(len(word)):
            if word[: i + 1] in word_dict and self.dfs(word[i + 1 :], word_dict):
                self.dp[word] = True
                return True
        self.dp[word] = False
        return False
