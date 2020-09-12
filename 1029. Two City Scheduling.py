from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a_total = 0
        b_total = 0
        total_cost = 0
        n = len(costs) // 2

        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

        for cost in costs:
            if cost[0] < cost[1]:
                if a_total < n:
                    total_cost += cost[0]
                    a_total += 1
                else:
                    total_cost += cost[1]
                    b_total += 1
            else:
                if b_total < n:
                    total_cost += cost[1]
                    b_total += 1

                else:
                    total_cost += cost[0]
                    a_total += 1
        return total_cost


if __name__ == "__main__":
    print(Solution().twoCitySchedCost([]))
    print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
    print(
        Solution().twoCitySchedCost(
            [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
        )
    )
    print(
        Solution().twoCitySchedCost(
            [
                [515, 563],
                [451, 713],
                [537, 709],
                [343, 819],
                [855, 779],
                [457, 60],
                [650, 359],
                [631, 42],
            ]
        )
    )
