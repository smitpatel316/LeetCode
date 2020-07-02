import collections
from typing import List


class Word:
    def __init__(self, word, changes):
        self.word = word
        self.changes = changes

    def increment(self):
        self.changes += 1

    def update(self, word):
        self.word = word


class Solution:
    def diff(self, a, b):
        return sum(a[i] != b[i] for i in range(len(a)))

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i]+"*"+word[i+1:]].append(word)
        queue = collections.deque([Word(beginWord, 1)])
        visited = set()
        while queue:
            next_word = queue.popleft()
            if next_word.word == endWord:
                return next_word.changes
            if next_word.word not in visited:
                visited.add(next_word.word)
                for i in range(len(word)):
                    neighbors = next_word.word[:i] + "*" + next_word.word[i+1:]
                    for neighbor in adj[neighbors]:
                        if neighbor not in visited:
                            queue.append(Word(neighbor, next_word.changes+1))
        return 0


if __name__ == "__main__":
    print(
        Solution().ladderLength(
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
        )
    )
