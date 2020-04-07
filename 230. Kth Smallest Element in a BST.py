# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return []
    else:
        return preorder(root.left) + [root.val] + preorder(root.right)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return preorder(root)[k-1]

if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.left.left = TreeNode(2)
    tree.left.left.left = TreeNode(1)
    print(Solution().kthSmallest(tree, 3))