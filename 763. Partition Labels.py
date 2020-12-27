from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []

        last_indexes = defaultdict(int)
        for i in range(len(S)):
            last_indexes[S[i]] = i

        l, r = 0, last_indexes[S[0]]
        partitions = []
        while r < len(S) and l < len(S):
            seen = set()
            start = l
            while l < r:
                if S[l] not in seen:
                    seen.add(S[l])
                    r = max(r, last_indexes[S[l]])
                l += 1
            partitions.append(r - start + 1)
            l = r + 1
            if l < len(S):
                r = last_indexes[S[l]]
        return partitions
