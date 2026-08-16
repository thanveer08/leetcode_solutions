# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = {}
        tempA = headA
        tempB = headB
        while tempA:
            visited[tempA] = True
            tempA = tempA.next
        while tempB:
            if tempB in visited:
                return tempB
            visited[tempB] = True
            tempB = tempB.next
        return None        
