# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        temp = l1
        while temp:
            arr1.append(temp.val)
            temp = temp.next

        arr2 = []
        temp = l2
        while temp:
            arr2.append(temp.val)
            temp = temp.next

        result = int("".join(str(n) for n in reversed(arr1))) + int("".join(str(n) for n in reversed(arr2)))

        dummy = ListNode(0)
        curr = dummy
        for digit in reversed(str(result)):
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next