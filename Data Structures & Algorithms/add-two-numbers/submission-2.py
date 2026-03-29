# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1 -> 2 -> 3 -> None = 321
        # 4 -> 5 -> 6 -> None = 654
        # 321 + 654 = 975

        # 1 -> 2 -> 3 -> 4 = 4321
        # 4 -> 5 -> 6 = 654


        p1 = l1
        p2 = l2
        length_l1 = 0
        length_l2 = 0

        carry = 0
        total = 0

        while p1 and p2:
            
            total = p1.val + p2.val + carry
            carry = math.floor(total // 10)
            total = total % 10

            length_l1 += 1
            length_l2 += 1

            p1.val = total
            p2.val = total            
            precursor = p1
            p1 = p1.next
            p2 = p2.next

        while p1:
            total = p1.val + carry
            carry = math.floor(total // 10)
            total = total % 10
            p1.val = total
            length_l1 += 1
            precursor = p1
            p1 = p1.next

        while p2:
            total = p2.val + carry
            carry = math.floor(total // 10)
            total = total % 10
            p2.val = total
            length_l2 += 1
            precursor = p2
            p2 = p2.next

        if carry != 0:
            remainder = ListNode(carry)
            precursor.next = remainder


        return l1 if length_l1 >= length_l2 else l2