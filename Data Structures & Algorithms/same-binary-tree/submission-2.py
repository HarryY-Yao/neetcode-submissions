# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s = [p]
        r = [q]

        while len(s) > 0 and len(r) > 0:
            curr1 = s.pop()
            curr2 = r.pop()

            if not curr1 and curr2:
                return False
            
            if not curr2 and curr1:
                return False

            if (curr1 and curr2) and curr1.val != curr2.val:
                return False
            
            if curr1:
                s.append(curr1.left)
                s.append(curr1.right)

            if curr2:
                r.append(curr2.left)
                r.append(curr2.right)

        return True