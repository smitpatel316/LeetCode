from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque(range(len(deck)))
        order = [None] * len(deck)

        for card in sorted(deck):
            order[q.popleft()] = card

            if q:
                q.append(q.popleft())
        return order
