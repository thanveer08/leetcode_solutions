# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while t1 or t2:
            sums = carry
            if t1:
                sums = sums+ t1.val
            if t2:
                sums = sums + t2.val
            new_node = ListNode(sums%10)
            carry = sums//10
            curr.next = new_node
            curr = curr.next
            if t1: 
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry:
            new_node = ListNode(carry)
            curr.next = new_node
            curr = curr.next                    
        return dummy.next