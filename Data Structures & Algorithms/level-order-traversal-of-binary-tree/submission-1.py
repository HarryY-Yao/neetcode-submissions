# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        res = []

        q.append(root)

        while len(q) > 0:
            qlen = len(q)
            
            curr_level = []
            for _ in range(len(q)):
                curr = q.popleft()

                if curr:
                    curr_level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)

            if len(curr_level) > 0:
                res.append(curr_level)

        return res