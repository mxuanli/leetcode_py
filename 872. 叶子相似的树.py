# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        node_list_1 = list()
        node_list_2 = list()

        def foo(root, node_list):
            if not root:
                return
            if not root.right and not root.left:
                node_list.append(root.val)
            foo(root.left, node_list)
            foo(root.right, node_list)

        foo(root1, node_list_1)
        foo(root2, node_list_2)
        return node_list_1 == node_list_2
