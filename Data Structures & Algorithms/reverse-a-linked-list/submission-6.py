# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        curr = head
        post = curr.next
        prev = None

        while post != None:
            curr.next = prev
            prev = curr
            curr = post
            post = post.next
        curr.next = prev
        
        return curr