# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def Gst(self, current, value):
        if current.right:
            value=self.Gst(current.right, value)
        
        value += current.val
        current.val = value

        if current.left:
            value=self.Gst(current.left, value)
        
        return value

    def bstToGst(self, root: TreeNode) -> TreeNode:

        self.Gst(root, 0)
        return root
    
left = TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3)))
right = TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8)))
test = TreeNode(4, left, right)
print(Solution().bstToGst(test).val) #only prints root value TODO print entire tree
        