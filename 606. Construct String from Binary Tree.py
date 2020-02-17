# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if root:
            result = str(root.val)
            if root.left:
                result += f"({self.tree2str(root.left)})"
            if root.right:
                if root.left is None:
                    result += "()"
                result += f"({self.tree2str(root.right)})"
            return result
        else:
            return ""
