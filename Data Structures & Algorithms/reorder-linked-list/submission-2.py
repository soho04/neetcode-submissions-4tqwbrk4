# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        mid = end = head

        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next

        p2 = mid.next
        mid.next = None
        previous = None

        while p2:
            next_node = p2.next
            p2.next = previous
            previous = p2
            p2 = next_node

        p1 = head
        p2 = previous

        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p1 = p1_next
            p2.next = p1
            p2 = p2_next

        #  p1                p2
        # [2, 4, 6] -> None [10, 8]

        

            