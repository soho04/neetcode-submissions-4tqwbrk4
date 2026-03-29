# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        p1 = head
        p2 = dummy
        count = 0

        while p1:
            p1 = p1.next
            count += 1

            if count > n:
                p2 = p2.next

        p2.next = p2.next.next

        return dummy.next


        
        #               p2
        #                              p1
        # dummy -> 1 -> 2 -> 3 -> 4 -> None
        # count = 3 


        # p2
        #               p1
        # dummy -> 5 -> None
        # count = 1
