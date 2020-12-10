from typings import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        _max = float("-inf")
        for account in accounts:
            _max = max(_max, sum(account))
        return _max
