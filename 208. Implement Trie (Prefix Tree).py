class TrieNode:
    def __init__(self, val="*", children=None, terminating=False):
        if children is None:
            children = {}
        self.children = children
        self.val = val
        self.terminating = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(val=c)
            curr = curr.children[c]
        curr.terminating = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr and curr.terminating

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
