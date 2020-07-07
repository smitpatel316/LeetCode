from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.counts = {}
        self.max_vals = []
        self.max_val = float("-inf")

    def get_sum(self, root):
        if not root:
            return 0

        total_sum = self.get_sum(root.left) + root.val + self.get_sum(root.right)
        if total_sum in self.counts:
            self.counts[total_sum] += 1
        else:
            self.counts[total_sum] = 1

        if self.counts[total_sum] > self.max_val:
            self.max_vals = []
            self.max_val = self.counts[total_sum]

        if self.counts[total_sum] == self.max_val:
            self.max_vals.append(total_sum)

        return total_sum

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.get_sum(root)
        return self.max_vals


if __name__ == "__main__":
    tree = TreeNode(5, TreeNode(2), TreeNode(-5))
    print(Solution().findFrequentTreeSum(tree))
