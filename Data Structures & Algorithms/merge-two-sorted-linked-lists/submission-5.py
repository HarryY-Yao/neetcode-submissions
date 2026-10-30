# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currDummy = dummy

        curr1 = list1
        curr2 = list2

        while curr1 != None and curr2 != None:
            if curr1.val >= curr2.val:
                currDummy.next = curr2
                curr2 = curr2.next
            else:
                currDummy.next = curr1
                curr1 = curr1.next
            currDummy = currDummy.next

        while curr1 != None and curr2 == None:
            currDummy.next = curr1
            currDummy = currDummy.next
            curr1 = curr1.next

        while curr2 != None and curr1 == None:
            currDummy.next = curr2
            currDummy = currDummy.next
            curr2 = curr2.next

        return dummy.next