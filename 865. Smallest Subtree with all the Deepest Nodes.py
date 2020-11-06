# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None, 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left[1] > right[1]:
                return left[0], left[1] + 1
            if left[1] < right[1]:
                return right[0], right[1] + 1
            return node, left[1] + 1

        return dfs(root)[0]


if __name__ == "__main__":
    t = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(2)), None)
    sol = Solution()
    print(sol.subtreeWithAllDeepest(t))
