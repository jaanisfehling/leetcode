# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        current = head
        size = 1
        while current.next is not None:
            current = current.next
            size += 1
        
        if size-n == 0:
            head = head.next
            return head

        current = head
        for i in range(size-n-1):
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        else:
            current = None

        return head
