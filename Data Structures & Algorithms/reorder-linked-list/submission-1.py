# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        ## Start of the second list

        second = slow.next 
        prev = slow.next = None

        ## Reverse
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first = head
        second = prev

        while first:
            print("first list: ", first.val)
            first = first.next

        while second:
            print("second list: ", second.val)
            second = second.next

        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            first = first.next
            second = temp2
            first.next = temp1
            first = first.next
            

        
        
        