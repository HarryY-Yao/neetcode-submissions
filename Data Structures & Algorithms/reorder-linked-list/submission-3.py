# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        currDummy = dummy
        original = head



        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length += 1

        if length <= 1:
            return
        
        prev = None
        curr = head
        for _ in range(length // 2):
            prev = curr
            curr = curr.next
        prev.next = None

        prev = None
        post = curr.next

        while post != None:
            curr.next = prev
            prev = curr
            curr = post
            post = post.next
        curr.next = prev



        while head != None and curr != None:
            currDummy.next = head
            currDummy = currDummy.next
            head = head.next

            currDummy.next = curr
            currDummy = currDummy.next
            curr = curr.next

        while head != None:
            currDummy.next = head
            currDummy = currDummy.next
            head = head.next

        while curr != None:
            currDummy.next = curr
            currDummy = currDummy.next
            curr = curr.next

        