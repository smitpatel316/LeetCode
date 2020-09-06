# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def recurse_tree(root):
            if not root:
                return False
            left = recurse_tree(root.left)
            right = recurse_tree(root.right)
            mid = root == p or root == q
            if mid + left + right >= 2:
                self.ans = root
            return mid or left or right

        recurse_tree(root)
        return self.ans
