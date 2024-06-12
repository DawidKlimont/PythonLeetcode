# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        solution=0
        cur = [root]
        while len(cur)>0:
            solution = 0
            cur_next = []

            for node in cur:
                solution += node.val 
                if node.left:
                    cur_next.append(node.left)
                if node.right:
                    cur_next.append(node.right)
            cur = cur_next
        return solution

left = TreeNode(2, TreeNode(4,TreeNode(7)), TreeNode(5))
right = TreeNode(3, None, TreeNode(6,None,(TreeNode(8))))
test = TreeNode(1, left, right)
print(Solution().deepestLeavesSum(test))