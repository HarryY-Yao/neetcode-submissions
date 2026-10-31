# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [root]

        while len(s) > 0:
            curr = s.pop()
            
            if curr != None:
                temp = curr.left
                curr.left = curr.right
                curr.right = temp

                s.append(curr.left)
                s.append(curr.right)

        return root