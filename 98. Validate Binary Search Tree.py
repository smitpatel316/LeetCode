import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNodeWrapper:
    def __init__(self, node: TreeNode, min_val, max_val):
        self.node = node
        self.min_val = min_val
        self.max_val = max_val


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque([])
        if root.left:
            if root.left.val >= root.val:
                return False
            else:
                queue.append(TreeNodeWrapper(root.left, float("-inf"), root.val - 1))

        if root.right:
            if root.right.val <= root.val:
                return False
            else:
                queue.append(TreeNodeWrapper(root.right, root.val + 1, float("inf")))

        while queue:
            node_wrapper = queue.popleft()
            node = node_wrapper.node
            min_val = node_wrapper.min_val
            max_val = node_wrapper.max_val
            if not (min_val <= node.val <= max_val):
                return False
            else:
                if node.left:
                    queue.append(TreeNodeWrapper(node.left, min_val, node.val - 1))
                if node.right:
                    queue.append(TreeNodeWrapper(node.right, node.val + 1, max_val))
        return True


if __name__ == "__main__":
    tree = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
    print(Solution().isValidBST(tree))
