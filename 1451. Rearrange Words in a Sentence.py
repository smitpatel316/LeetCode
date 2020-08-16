class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text = text.split(" ")
        text = [(word, i) for i, word in enumerate(text)]
        text = sorted(text, key=lambda x: (len(x[0]), x[1]))
        res = ""
        for (word, i) in text:
            res += f" {word}"
        return res[1].upper() + res[2:]


if __name__ == "__main__":
    print(Solution().arrangeWords("Leetcode is cool"))
    print(Solution().arrangeWords("Keep calm and code on"))
    print(Solution().arrangeWords("To be or not to be"))
