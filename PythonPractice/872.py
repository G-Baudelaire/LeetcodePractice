# Definition for a binary tree node.
from itertools import zip_longest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        dummy_node = TreeNode(val=None)
        for leaf1, leaf2, in zip_longest(self.getLeaves(root1), self.getLeaves(root2), fillvalue=dummy_node):
            print(leaf1, leaf2)
            if leaf1.val != leaf2.val:
                return False
        return True

    def getLeaves(self, root):
        queue = [root]
        while queue:
            node = queue.pop()
            if not node.left and not node.right:
                yield node
                continue

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)
