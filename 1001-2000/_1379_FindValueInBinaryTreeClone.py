class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original.val == target.val:
            return cloned

        if original.left:
            left = self.getTargetCopy(original.left, cloned.left, target)
            if left:
                return left

        if original.right:
            right = self.getTargetCopy(original.right, cloned.right, target)
            if right:
                return right

        return None
    
left = TreeNode(4)
right = TreeNode(3, TreeNode(6), TreeNode(19))
test = TreeNode(7, left, right)

left_clone = TreeNode(4)
right_clone = TreeNode(3, TreeNode(6), TreeNode(19))
test_clone= TreeNode(7, left, right)

print(Solution().getTargetCopy(test,test_clone,right).val)