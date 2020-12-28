from collections import Counter
import string
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        punctdict = dict()

        mys = ""
        for sign in string.punctuation:
            punctdict[sign] = " "
            mys += " "

        paragraph = paragraph.translate(str.maketrans(string.punctuation, mys))
        banned = set(banned)
        counter = Counter(paragraph.split())

        max_count = float("-inf")
        res = None
        for word in counter:
            if word not in banned:
                if res is None or counter[word] > max_count:
                    res = word
                    max_count = counter[word]
        return res
