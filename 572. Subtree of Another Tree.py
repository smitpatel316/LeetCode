# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.preorder(t) in self.preorder(s)

    def preorder(self, tn: TreeNode) -> str:
        if tn is None:
            return "None"
        else:
            return f"#{tn.val} {self.preorder(tn.left)} {self.preorder(tn.right)}"
