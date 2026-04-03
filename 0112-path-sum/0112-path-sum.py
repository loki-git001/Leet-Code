# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stk = [(root, root.val)]

        while stk:
            node, curr_sum = stk.pop()

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True
            
            if node.left:
                stk.append([node.left, node.left.val + curr_sum])
            if node.right:
                stk.append([node.right, node.right.val + curr_sum])

        return False