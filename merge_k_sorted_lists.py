# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        remove_indices = []
        for i in range(len(lists)):
            if lists[i] is None:
                remove_indices.append(i)
        for i in range(len(remove_indices)):
            del lists[remove_indices[i]-i]
        if not lists:
            return None

        candidate = 0
        for i in range(len(lists)):
            if lists[i].val < lists[candidate].val:
                candidate = i
        current = ListNode(lists[candidate].val)
        result = current
        lists[candidate] = lists[candidate].next
        if lists[candidate] is None:
            del lists[candidate]

        while lists:
            candidate = 0
            for i in range(len(lists)):
                if lists[i].val < lists[candidate].val:
                    candidate = i
            current.next = ListNode(lists[candidate].val)
            current = current.next
            lists[candidate] = lists[candidate].next
            if lists[candidate] is None:
                del lists[candidate]
        return result
