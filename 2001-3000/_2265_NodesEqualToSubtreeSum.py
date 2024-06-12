#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    solution = 0
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.solution=0
        self.traverse(root)

        return self.solution

    def traverse(self, current: TreeNode):
        left = [0,0]
        if current.left:
            left = self.traverse(current.left)
        right=[0,0]
        if current.right:
            right = self.traverse(current.right)

        complete = [current.val+left[0]+right[0],1+left[1]+right[1]]
        if left[1]+right[1]==0 or current.val == complete[0]//complete[1]:
            self.solution+=1
        return complete