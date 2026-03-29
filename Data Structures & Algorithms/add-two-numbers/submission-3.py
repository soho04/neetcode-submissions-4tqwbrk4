# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        carry = 0

        dummy = ListNode(0)
        curr = dummy

        while p1 or p2 or carry:

            running_sum = 0

            if p1:
                running_sum += p1.val
                p1 = p1.next
            
            if p2:
                running_sum += p2.val
                p2 = p2.next

            if carry:
                running_sum += carry

            print(running_sum)

            carry = running_sum // 10
            running_sum = running_sum % 10

            node = ListNode(running_sum)
            curr.next = node
            curr = curr.next

        return dummy.next

        # 1 -> 2 -> 3 -> None = 321
        # 4 -> 5 -> 6 -> None = 654
        # 321 + 654 = 975

        # 1 -> 2 -> 3 -> 4 = 4321
        # 4 -> 5 -> 6 = 654


        