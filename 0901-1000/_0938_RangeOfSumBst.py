from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        solution=0
        if root.val>=low and root.val <= high:
            solution+=root.val
        if root.left and not root.val < low:
            solution+=self.rangeSumBST(root.left,low,high)
        if root.right and not root.val > high:
            solution+= self.rangeSumBST(root.right,low,high)
        return solution


left = TreeNode(5, TreeNode(3), TreeNode(7))
right = TreeNode(15, None, TreeNode(18))
test = TreeNode(10, left, right)
print(Solution().rangeSumBST(test,7,15))