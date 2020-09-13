from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += (b,)
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]


if __name__ == "__main__":
    print(
        Solution().findItinerary(
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        )
    )
    print(
        Solution().findItinerary(
            [
                ["JFK", "SFO"],
                ["JFK", "ATL"],
                ["SFO", "ATL"],
                ["ATL", "JFK"],
                ["ATL", "SFO"],
            ]
        )
    )
    print(Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
    print(
        Solution().findItinerary(
            [
                ["JFK", "AAA"],
                ["AAA", "JFK"],
                ["JFK", "BBB"],
                ["JFK", "CCC"],
                ["CCC", "JFK"],
            ]
        )
    )
    print(
        Solution().findItinerary(
            [
                ["EZE", "TIA"],
                ["EZE", "HBA"],
                ["AXA", "TIA"],
                ["JFK", "AXA"],
                ["ANU", "JFK"],
                ["ADL", "ANU"],
                ["TIA", "AUA"],
                ["ANU", "AUA"],
                ["ADL", "EZE"],
                ["ADL", "EZE"],
                ["EZE", "ADL"],
                ["AXA", "EZE"],
                ["AUA", "AXA"],
                ["JFK", "AXA"],
                ["AXA", "AUA"],
                ["AUA", "ADL"],
                ["ANU", "EZE"],
                ["TIA", "ADL"],
                ["EZE", "ANU"],
                ["AUA", "ANU"],
            ]
        )
    )
