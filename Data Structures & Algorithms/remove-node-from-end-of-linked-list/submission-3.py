# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        length = 0
        count = head
        while count != None:
            count = count.next
            length += 1

        curr = head
        post = curr.next
        prev = None

        for _ in range(length - n):
            prev = curr
            curr = curr.next
            post = post.next

        if prev != None:
            prev.next = post
        else:
            head = head.next
        

        return head

