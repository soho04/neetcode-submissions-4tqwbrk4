# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        dummy = ListNode(0, head)

        curr = dummy

        fast = head

        while fast and fast.next:

            fast = fast.next.next
            curr = curr.next

        mid = curr.next
        curr.next = None

        previous = None

        while mid:
            nxt = mid.next
            mid.next = previous
            previous = mid
            mid = nxt

        curr = dummy.next

        while curr and curr.next and previous and previous.next:

            nxt = curr.next
            curr.next = previous
            prev_next = previous.next
            previous.next = nxt
            previous = prev_next
            curr = nxt

        if previous:
            if curr:
                curr.next = previous
        
            
           

        # c  nxt
        # 2, 4
        #     p
        # 10, 8, 6


        

            