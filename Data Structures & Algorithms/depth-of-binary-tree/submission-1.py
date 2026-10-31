# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        s = [root]
        root.val = 1
        max_depth = 0

        while len(s) > 0:
            curr = s.pop()
            max_depth = max(max_depth, curr.val)

            if curr.left:
                curr.left.val = curr.val + 1
                s.append(curr.left)
            
            if curr.right:
                curr.right.val = curr.val + 1
                s.append(curr.right)
        
        return max_depth