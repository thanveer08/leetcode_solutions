# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        tempA = headA
        tempB = headB
        while(tempA!= tempB):
            tempA = tempA.next
            tempB = tempB.next

            if tempA == tempB :
                return tempA
            if tempA == None:
                tempA = headB
            if tempB == None:
                tempB = headA
        return tempA                