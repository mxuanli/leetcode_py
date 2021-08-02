# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        self.dict_node = defaultdict(lambda: defaultdict(list))

        def foo(root, line, row):
            if root == None:
                return
            foo(root.left, line - 1, row + 1)
            self.dict_node[line][row].append(root.val)
            foo(root.right, line + 1, row + 1)
            return

        foo(root, 0, 0)
        r = list()
        for i in sorted(self.dict_node):
            tmp = list()
            line_node = self.dict_node[i]
            for j in sorted(line_node):
                tmp += sorted(line_node[j])
            r.append(tmp)
        return r
